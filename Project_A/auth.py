from flask import Blueprint, render_template, redirect, url_for, request, flash

from __init__ import db
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST']) # define login page path
def login(): # define login page fucntion
    if request.method=='GET': # if the request is a GET we return the login page
        return render_template('login.html')
    else: # if the request is POST the we check if the user exist
          # and with te right password
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        user = User.query.filter_by(email=email).first()
        # check if the user actually exists
        # take the user-supplied password, hash it, and compare it
        # to the hashed password in the database
        if not user:
            flash('Please sign up before!')
            return redirect(url_for('auth.signup'))
        elif not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login')) # if the user
               #doesn't exist or password is wrong, reload the page
        # if the above check passes, then we know the user has the
        # right credentials
        login_user(user, remember=remember)
        return redirect(url_for('main.profile'))

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
        # new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
        new_user = User(email=email, name=name, password=generate_password_hash(password), account_balance=50)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))

@auth.route('/deposit', methods=['GET', 'POST'])
@login_required
def deposit(): # define the sign up function
    if request.method=='GET': # If the request is GET we return the
                              # sign up page and forms
        return render_template('deposit.html')
    else:
        deposit = request.form.get('deposit')
        current_user.account_balance += float(deposit)
        db.session.commit()
        return redirect(url_for('auth.deposit'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))