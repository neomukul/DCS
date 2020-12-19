from flask import Flask
import os
import random

app = Flask(__name__)

@app.route("/")
def display():
    return "Welcome to DCS task 1"


if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
    app.run(port=3000, host="0.0.0.0")
