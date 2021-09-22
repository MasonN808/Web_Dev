from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from models import User
import pandas as pd


# Initialize the SQLAlchemy
db = SQLAlchemy()

def make_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'data-key-here'
    # Save sql database at this path
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    # initialize the sqlite database
    db.init_app(app)
    # Create instance of login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

@login_manager.user_loader




if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, debug=True)
    app.run(debug=True)
