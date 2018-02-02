from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp
from datetime import datetime

from helpers import *

# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# custom filter
app.jinja_env.filters["usd"] = usd

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

@app.route("/")
@login_required
def index():

    # select user's cash balance
    id = session["user_id"]
    cash = db.execute("SELECT cash FROM users WHERE id = :id", id=id)
    totalvalue = cash[0]["cash"]

    # select stock symbol and number of shares from user's portfolio
    portfolio = db.execute("SELECT symbol, shares FROM portfolio WHERE id = :id", id=id)

    # for every stock in portfolio, assign dictionary key/values pairs for use in jinja
    for stock in portfolio:
        symbol = str(stock["symbol"])
        shares = int(stock["shares"])
        quote = lookup(symbol)
        stock["name"] = quote["name"]
        stock["price"] = round(quote["price"],2)
        stock["total"] = round(quote["price"] * shares,2)
        stock["totalvalue"] = quote["price"] * shares
        totalvalue += stock["totalvalue"]

    # render index page to see stock symbol, name, shares, price, and total
    return render_template("index.html", portfolio=portfolio, cash=cash, totalvalue=totalvalue)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock."""

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "GET":
        return render_template("buy.html")
    else:
        # ensure user entered a symbol and shares
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        if not symbol or not shares:
            return apology("Must input stock ticker and shares")

        # use lookup function to get stock info
        stock = lookup(request.form.get("symbol"))
        if not stock:
            return apology("Stock does not exist")

        # make sure user inputs valid number of shares
        price = float(stock["price"])
        shares = int(shares)
        if shares <= 0:
            return apology("Shares must be positive integer")

        # select user's cash balance
        id = session["user_id"]
        rows = db.execute("SELECT * FROM users WHERE id = :id", id=id)
        cash = float(rows[0]["cash"])

        # total cost of purchase
        purchase = float(stock["price"] * float(shares))

        # does user have enough cash?
        if cash < purchase:
            return apology("You don't have enough money")

        # if user has enough cash, update user's cash, their portfolio, and history tables
        else:
            db.execute("UPDATE users SET cash = cash - :purchase WHERE id = :id",
                        purchase=purchase, id=id)
            db.execute("UPDATE portfolio SET shares = shares + :shares WHERE id = :id AND symbol = :symbol",
                        shares=shares, id=id, symbol=symbol)
            db.execute("INSERT OR IGNORE INTO portfolio (id,symbol,shares) VALUES (:id,:symbol,:shares)",
                        id=id, symbol=symbol, shares=shares)
            db.execute("INSERT INTO history (id,symbol,shares,price,timestamp) \
                        VALUES (:id,:symbol,:shares,:price,:timestamp)",
                        id=id, symbol=symbol, shares=shares, price=price, timestamp=str(datetime.now()))

        flash('Bought!')
        return redirect(url_for("index"))


@app.route("/history")
@login_required
def history():
    """Show history of transactions."""

    # obtain stock info from portfolio database
    history = db.execute("SELECT * FROM history WHERE id = :id ORDER BY timestamp ASC", id=session["user_id"])

    # for every stock in the user's portfolio, assign dict key/values for use in html/jinja
    for transaction in history:
        symbol = transaction["symbol"]
        shares = transaction["shares"]
        price = transaction["price"]
        timestamp = transaction["timestamp"]

    return render_template("history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
            return apology("invalid username and/or password")

        # remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # if nothing was entered return apology
        if not request.form.get("quote"):
            return apology("please enter a stock ticker")

        # look up stock using lookup function in helpers.py
        result = lookup(request.form.get("quote"))
        name = result["name"]
        symbol = result["symbol"]
        price = result["price"]

        # check if stock is real
        if not result:
            return apology("the stock does not exist or the ticket symbol you entered is incorrect.")

        # render webpage to see quote name, price, symbol
        return render_template("quoted.html", name=name, symbol=symbol, price=price)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""

    # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("Missing username!")

        # ensure password was submitted make sure password and confirmation match
        elif not request.form.get("password"):
            return apology("Missing username")

        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("Passwords don't match!")

        # encrpyt password
        hash = pwd_context.hash(request.form.get("password"))

       # log user to database or return apology if username already exits
        result = db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)",
                            username=request.form.get("username"), hash=hash)
        if not result:
            return apology("username already exists")

        # remember which user has logged in
        session["user_id"] = result

        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock."""

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "GET":
        return render_template("sell.html")
    else:
        # ensure user entered a symbol and shares
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        if not symbol or not shares:
            return apology("Must input stock ticker and shares")

        # use lookup function to get stock info
        quote = lookup(request.form.get("symbol"))
        if not quote:
            return apology("Stock does not exist")

        # make sure user inputs valid number of shares
        shares = int(shares)
        if shares <= 0:
            return apology("Shares must be positive integer")

        # initialize variables
        symbol = quote["symbol"]
        id = session["user_id"]
        stocks = []

        # select user's stock info from portfolio
        stocks = db.execute("SELECT shares FROM portfolio WHERE id = :id AND symbol = :symbol",
                            id=id, symbol=symbol)

        # ensure user owns stock and enough shares
        if stocks == []:
            return apology("This stock does not exist in your portfolio")
        if shares > stocks[0]["shares"]:
            return apology("You don't own this many shares")

        # calculate current price per share and cost of all shares that user owns
        price = round(float(quote["price"]),2)
        cost = round(float(shares * price),2)

        # update user's cash balance
        db.execute("UPDATE users SET cash = cash + :cost WHERE id = :id",
                    cost=cost, id=id)

        # if there are shares leftover after sale, update row in user's porfolio
        if shares < stocks[0]["shares"]:
            db.execute("UPDATE portfolio SET shares = shares - :shares WHERE id = :id AND symbol = :symbol",
                        id=id, shares=shares, symbol=symbol)

        # if there are no leftover shares, delete row from portfolio
        elif shares == stocks[0]["shares"]:
            db.execute("DELETE FROM portfolio WHERE id = :id AND symbol = :symbol",
                        id=id, symbol=symbol)

        # update user's history to reflect changes after sale
        db.execute("INSERT INTO history (id,symbol,shares,price,timestamp) \
                    VALUES (:id,:symbol,:shares,:price,:timestamp)",
                    id=id, symbol=symbol, shares=-shares, price=price, timestamp=str(datetime.now()))

        flash('Sold!')
        return redirect(url_for("index"))


@app.route("/deposit", methods=["GET", "POST"])
@login_required
def deposit():
    """Deposit cash into account."""

    # if user reached route via GET, return deposit page
    if request.method == "GET":
        return render_template("deposit.html")

    # if user reached via POST i.e. submitting form, check that the form is valid
    elif request.method == "POST":
        if not request.form.get("amount"):
            return apology("You must provide amount")
        if not request.form.get("amount").isdigit():
            return apology("Invalid amount")

        # update user's cash amount
        db.execute("UPDATE users SET cash = cash + :amount WHERE id = :id",
                    amount = request.form.get("amount"), id=session["user_id"])

        flash("Cash desposit successful!")

        return redirect(url_for("index"))


@app.route("/withdrawl", methods=["GET", "POST"])
@login_required
def withdrawl():
    """Deposit cash into account."""

    # if user reached route via GET, return deposit page
    if request.method == "GET":
        return render_template("withdrawl.html")

    # if user reached via POST i.e. submitting form, check that the form is valid
    elif request.method == "POST":
        if not request.form.get("amount"):
            return apology("You must provide amount")
        if not request.form.get("amount").isdigit():
            return apology("Invalid amount")

        # update user's cash amount
        db.execute("UPDATE users SET cash = cash - :amount WHERE id = :id",
                    amount = request.form.get("amount"), id=session["user_id"])

        flash("Cash withdrawl successful!")

        return redirect(url_for("index"))

