from flask import Blueprint, render_template, redirect, url_for, request, flash

from __init__ import db
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user


auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET'])
def login():
    return render_template('login.html')

# @auth.route('/signup', methods = ['GET'])
# def signup():
#     return render_template('signup.html')

# @auth.route('/logout')
# def logout():
#     return 'logout'

@auth.route('/signup', methods=['GET', 'POST'])
def signup(): # define the sign up function
    if request.method=='GET': # If the request is GET we return the
                              # sign up page and forms
        return render_template('signup.html')
    else: # if the request is POST, then we check if the email
          # doesn't already exist and then we save data
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first() # if this
                              # returns a user, then the email
                              # already exists in database
        if user: # if a user is found, we want to redirect back to
                 # signup page so user can try again
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))
        # create a new user with the form data. Hash the password so
        # the plaintext version isn't saved.
        new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))