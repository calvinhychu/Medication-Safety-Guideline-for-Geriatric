# library.py
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home</h1>"


@app.route("/about")
def about():
    return "About!"


if __name__ == "__main__":
    app.run()
