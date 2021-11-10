from flask import Blueprint, render_template
from __init__ import create_app, mysql
from flask_login import login_required, current_user
import sqlite3
import csv
import sqlalchemy as sqAl
from sqlalchemy import inspect
# from models import User
import sqlalchemy.orm as orm

# Main blueprint
main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name = current_user.name, email = current_user.email,
                           password = current_user.password, account_balance = current_user.account_balance)

# @main.route('/deposit')
# @login_required
# def deposit():
#     return render_template('deposit.html')

# make app
app = create_app()

if __name__ == '__main__':

    # mysql.create_all(app=create_app())  # create the SQLite database
    app.run(debug=True)  # run the flask app on debug mode

