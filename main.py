# library.py
from flask import Flask, render_template, request, flash, session, redirect, \
    url_for
from flask_bootstrap import Bootstrap
from forms import register
app = Flask(__name__)
app.config['SECRET_KEY'] = 'f9bf78b9a18ce6d46a0cd2b0b86df9da'

Bootstrap(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')



@app.route("/register", methods=["POST", "GET"])
def register():
    form = register(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        return 'We confirm your registration!'
    return render_template('login.html', form=form)



@app.route("/login", methods=["POST", "GET"])
def login():
    flash('Account successfully registered! Login to access your account.')
    return render_template('login.html')




'''
app.route('/medications/<med>')
def show_med_information(med):
    # show the user profile for that user
    return 'User %s' % escape(med)
'''


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run()
