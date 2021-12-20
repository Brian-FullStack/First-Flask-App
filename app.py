import os
import json
from flask import Flask, render_template #Importing Flask class


app = Flask(__name__) #Storing an instance of Flask in the app variable


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

@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
    