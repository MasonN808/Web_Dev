from flask_login import UserMixin
from __init__ import mysql

# UserMixin gives data on the user, checking whether the user is anonymous, logged in, signed up, et.
# class User():
#     id = mysql.Column(mysql.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
#     email = mysql.Column(mysql.String(100), unique=True)
#     password = mysql.Column(mysql.String(100))
#     name = mysql.Column(mysql.String(1000))
#     account_balance = mysql.Column(mysql.Float)
