  
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
from flask_sqlalchemy import SQLAlchemy 
from flask_bootstrap import Bootstrap
from flask_mail import Mail, Message

login_manager = LoginManager()
db = SQLAlchemy()
mail = Mail()
Bootstrap = Bootstrap()