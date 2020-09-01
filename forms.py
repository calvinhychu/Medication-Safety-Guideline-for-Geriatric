from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired, InputRequired, Length, Email


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    profession = SelectField('Profession', choices=[('1', 'Physician'), ('2', 'Pharmacist'), ('3', 'Nurse Practioner')])
    department = StringField('Department', validators=[DataRequired()])
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])