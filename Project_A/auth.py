from flask import Blueprint, render_template, redirect, url_for, request, flash


auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET'])
def login():
    return 'login'

@auth.route('/signup', methods = ['GET'])
def signup():
    return 'signup'

@auth.route('/logout')
def logout():
    return 'logout'