import os
import json
from flask import Flask, render_template, request, flash#Importing Flask class
if os.path.exists("env.py"):
    import env


app = Flask(__name__) #Storing an instance of Flask in the app variable
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/gods.json", "r") as json_data: #opening the JSON file as read-only and passing the contents of that file to the variable json_data
        data = json.load(json_data)
    return render_template("about.html", page_title="About", gods=data)


@app.route("/about/<greekGod_name>")    
def about_greekGod(greekGod_name):
    greekGod = {}
    with open("data/gods.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == greekGod_name:
                greekGod = obj
    return render_template("greekGod.html", greekGod = greekGod)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have recieved your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
    