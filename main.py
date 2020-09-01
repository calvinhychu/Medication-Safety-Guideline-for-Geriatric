from flask import Flask, render_template, request, flash, session, redirect, \
    url_for
from flask_bootstrap import Bootstrap
from forms import *
from flask_sqlalchemy  import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from secret_key import *
import datetime
import os

file_path = os.path.abspath(os.getcwd())+"\stjoegeriatric.db"


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path

Bootstrap(app)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    profession = db.Column(db.String(30), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80))
    # posts = db.relationship('Post', backref='author', lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # date_posted = db.Column(db.Date, nullable=False, default=datetime.now)
    content = db.Column(db.Text, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')



@app.route("/register", methods=["POST", "GET"])
def register():
    if current_user.is_authenticated:
        flash('Please logged out before sign-up.')
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(name=form.name.data, profession=form.profession.data, department=form.department.data,
        email=form.email.data, password=hashed_password)
        try:
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError:
            flash('Email already registered!')
            return redirect(url_for('register'))
        flash('Account successfully registered! Login to access your account.')
        return redirect(url_for('login'))


    return render_template('register.html', form=form)



@app.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        flash('Already Logged in!')
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user_email = User.query.filter_by(email=form.email.data).first()
        if user_email and check_password_hash(user_email.password, form.password.data):
                login_user(user_email)
                flash('Logged in succesfully.')
                return redirect(url_for('home'))
        else:
            flash('Invalid email or password')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out succesfully.')
    return redirect(url_for('home'))


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
    db.create_all()
    app.run()
