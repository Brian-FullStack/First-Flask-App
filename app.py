import os
from flask import Flask #Importing Flask class


app = Flask(__name__) #Storing an instance of Flask in the app variable


@app.route("/")
def index():
    return "Hello, World"



if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
    