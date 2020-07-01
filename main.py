# library.py
from flask import Flask, render_template, request
import sql
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'GET':
        return render_template("login.html")



'''
app.route('/medications/<med>')
def show_med_information(med):
    # show the user profile for that user
    return 'User %s' % escape(med)
'''


@app.route("/about")
def about():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
