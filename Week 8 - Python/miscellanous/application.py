# We can use a framework, a collection of code that contains even more functionality 
# that we can use to build projects on top of.

# One such framework is Flask, which has some basic functionality we can use. 
# A basic application will look something like this:

from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    if request.form["name"] == "" or request.form["dorm"] == "":
        return render_template("failure.html")
    return render_template("success.html")

# We first import lots of functionality from flask, and create an app.

# Then we have a line @app.route("/") that says the next function should 
# be called whenever that path on the web server is requested. In this case, 
# the function will return render_template("index.html"), or whatever the file 
# index.html looks like.

# Then if we see @app.route("/register", methods=["POST"]), someone sending a 
# POST request to /register, we’ll call the register function underneath. 
# That function, if we don’t have certain elements in the form, will return the 
# template failure.html. Otherwise, it’ll return success.html.