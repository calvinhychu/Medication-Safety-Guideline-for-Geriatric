# from flask_sqlalchemy  import SQLAlchemy
# from flask_login import UserMixin
# from main import app
# import datetime
# db = SQLAlchemy(app)

# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(), nullable=False)
#     profession = db.Column(db.String(), nullable=False)
#     department = db.Column(db.String(), nullable=False)
#     email = db.Column(db.String(50), unique=True, nullable=False)
#     password = db.Column(db.String(80))
#     notes = db.relationship('Note', backref='user')

# class Note(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.Text, nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     drug_id = db.Column(db.Integer, db.ForeignKey('drug.id'))
#     drugclass_id = db.Column(db.Integer, db.ForeignKey('drugclass.id'))
    
# class Drugclass(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(), unique=True, nullable=False)
#     beers_criteria = db.Column(db.Text, nullable=True)
#     stopp_start_criteria = db.Column(db.Text, nullable=True)
#     drugs = db.relationship('Drug', backref='drugclass')
#     notes = db.relationship('Note', backref='drugclass')

# class Drug(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(), unique=True, nullable=False)
#     beers_criteria = db.Column(db.Text, nullable=True)
#     stopp_start_criteria = db.Column(db.Text, nullable=True)
#     drug_class_id = db.Column(db.Integer, db.ForeignKey('drugclass.id')) 
#     notes = db.relationship('Note', backref='drug')