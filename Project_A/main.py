from flask import Blueprint, render_template
from __init__ import create_app, db
from flask_login import login_required, current_user
import sqlite3
import csv
import sqlalchemy as sqAl
from sqlalchemy import inspect
from models import User
import sqlalchemy.orm as orm

# Main blueprint
main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')

# Testing of login route
# @main.route('/login')
# def login():
#     return render_template('login.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name = current_user.name)

# Testing of signup route
# @main.route('/signup')
# def signup():
#     return render_template('signup.html')


# make app
app = create_app()

if __name__ == '__main__':
    # dbfile = 'data.db'
    # outfile = open('mydump.csv', 'wb')
    # outcsv = csv.writer(outfile)
    # # Create a SQL connection to our SQLite database
    # con = sqlite3.connect(dbfile)
    #
    # # creating cursor
    # # Now in order to read in pandas dataframe we need to know table name
    # cursor = con.cursor()
    # cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # print(f"Table Name : {cursor.fetchall()}")
    #
    # con.close()

    with open("mydump.csv", 'w') as file:
        out_csv = csv.writer(file, lineterminator='\n')

        columns = [column.name for column in inspect(User).columns][1:]
        out_csv.writerow(columns)

        session_3 = orm.sessionmaker()

        extract_query = [getattr(User, col) for col in columns]
        for mov in session_3.query(*extract_query):
            out_csv.writerow(mov)

        session_3.close()


    # with open('mydump.csv', 'w') as f:
    #     out = csv.writer(f)
    #
    #     out.writerow(['id', 'email', 'password', 'name'])
    #     for item in session.query(Queue).all():
    #         out.writerow([User.id, User.email, User.password, User.name])
    #
    #

    db.create_all(app=create_app())  # create the SQLite database
    app.run(debug=True)  # run the flask app on debug mode
    # con = sqlite3.connect('data.db')
    # outfile = open('mydump.csv', 'wb')
    # outcsv = csv.writer(outfile)
    #
    # cursor = con.execute('select * from mytable')
    #
    # # dump column titles (optional)
    # outcsv.writerow(x[0] for x in cursor.description)
    # # dump rows
    # outcsv.writerows(cursor.fetchall())
    #
    # outfile.close()
