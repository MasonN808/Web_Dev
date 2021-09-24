from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from models import User
from auth import auth as auth_blueprint
from main import main as main_blueprint
from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from __init__ import create_app
import pandas as pd


# Main blueprint
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'index'

@main.route('/profile')
def profile():
    return 'profile'

# make app

app = create_app()


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, debug=True)
    app.run(debug=True)
