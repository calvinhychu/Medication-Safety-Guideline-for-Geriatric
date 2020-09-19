from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Length, Email, ValidationError

def check_email_domain(form, field):
    if field.data[-17:] != '@stjoestoronto.ca':
        raise ValidationError('Email must be under domain of @stjoestoronto.ca')

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    profession = SelectField('Profession', choices=[('Physician', 'Physician'), ('Pharmacist', 'Pharmacist'), ('Nurse Practioner', 'Nurse Practioner')])
    department = StringField('Department', validators=[DataRequired()])
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=80)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=80)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])

class NoteForm(FlaskForm):
    content = TextAreaField('content', render_kw={"rows": 5, "cols": 1}, validators=[InputRequired()])