from flask_login import UserMixin
from __init__ import db

# UserMixin gives data on the user, checking whether the user is anonymous, logged in, signed up, et.
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    account_balance = db.Column(db.Numeric)
