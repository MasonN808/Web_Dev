# from flask import Blueprint, render_template
# from __init__ import create_app, mysql
# from flask_login import login_required, current_user
# import sqlite3
# import csv
# import sqlalchemy as sqAl
# from sqlalchemy import inspect
# # from models import User
# import sqlalchemy.orm as orm
#
# # Main blueprint
# main = Blueprint('main', __name__)
#
#
# @main.route('/')
# def index():
#     return render_template('index.html')
#
#
# @main.route('/profile')
# @login_required
# def profile():
#     return render_template('profile.html', name = current_user.name, email = current_user.email,
#                            password = current_user.password, account_balance = current_user.account_balance)
#
# # @main.route('/deposit')
# # @login_required
# # def deposit():
# #     return render_template('deposit.html')
#
# # make app
# app = create_app()

from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import login_required, LoginManager
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
# For user ids
import uuid

app = Flask(__name__)

app.secret_key = '12345'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'Mason'
app.config['MYSQL_PASSWORD'] = 'Pancakes808'
app.config['MYSQL_DB'] = 'investment'

mysql = MySQL(app)

# login_manager = LoginManager()
# login_manager.login_view = '/login'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE User_EMAIL = % s AND User_PASSWORD = % s', (email, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['User_ID']
            session['email'] = account['User_EMAIL']
            session['name'] = account['User']
            session['account_balance'] = 50 #CHANGE LATER
            msg = 'Logged in successfully !'
            return profile()
        else:
            msg = 'Incorrect email / password !'
    return render_template('login.html', msg=msg)


@app.route('/profile')
def profile():
    if session.get('loggedin') == True:
        return render_template('profile.html', name = session['name'], email = session['email'],
                        account_balance = session['account_balance'])
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    # session['loggedin'] = False
    session.pop('id', None)
    session.pop('email', None)
    return redirect(url_for('index'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    msg = ''
    if request.method == 'POST' and 'password' in request.form and 'email' in request.form and 'name' in request.form:
        password = request.form['password']
        email = request.form['email']
        name = request.form['name']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE USER_EMAIL = % s', (email, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not password or not email or not name:
            msg = 'Please fill out the form !'
        else:
            user_id = str(uuid.uuid4())
            cursor.execute('INSERT INTO users VALUES (% s, % s, % s, % s)', (name, user_id, email, password,))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('signup.html', msg = msg)

@app.route('/deposit', methods=['GET', 'POST'])
def deposit(): # define the sign up function
    if request.method=='GET': # If the request is GET we return the
                              # sign up page and forms
        return render_template('deposit.html')
    else:
        deposit = request.form.get('deposit')
        session['account_balance'] += float(deposit)
        session['account_balance'] = round(session['account_balance'], 2)
        return redirect(url_for('main.profile'))


if __name__ == '__main__':
    # mysql.create_all(app=create_app())  # create the SQLite database
    app.run(debug=True)  # run the flask app on debug mode

