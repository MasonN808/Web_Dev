from flask import Blueprint, render_template, redirect, url_for, request, flash

from __init__ import db
auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET'])
def login():
    return render_template('login.html')

@auth.route('/signup', methods = ['GET'])
def signup():
    return render_template('signup.html')

@auth.route('/logout')
def logout():
    return 'logout'