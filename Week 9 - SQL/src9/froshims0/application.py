# Let’s look at froshims0, which has a templates directory with 
# various files ending in .html, as well as application.py:

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    if request.form["name"] == "" or request.form["dorm"] == "":
        return render_template("failure.html")
    return render_template("success.html")

# We added a register function that will respond differently
#  based on the user’s input.

# In this case, we will check whether the HTTP request, submitted 
# with a POST method, has a form with a name and dorm field, and if 
# either are blank, return the template failure.html, otherwise success.html.