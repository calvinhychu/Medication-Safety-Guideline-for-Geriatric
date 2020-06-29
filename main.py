# library.py
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return "Hello world from Flask!"


if __name__ == "__main__":
    app.run()
