# To actually store our data, let’s look at application.py in froshims1:



from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    if request.form["name"] == "" or request.form["dorm"] == "":
        return render_template("failure.html")
    file = open("registrants.csv", "a")
    writer = csv.writer(file)
    writer.writerow((request.form["name"], request.form["dorm"]))
    file.close()
    return render_template("success.html")

# Notice that in the final lines of register(), we write the information 
# we get from the request into a file called registrants.csv, 
# in a comma-separated values file format.

# To do this, we open the file, and the second argument, a, appends to the file,
#  or adds to the end. If we used w for writing, we’d overwrite the previous file 
#  with a new one.

# Then we use a csv module that comes with Python to write to the file, calling a 
# method writerow that actually does the writing of the name and dorm.