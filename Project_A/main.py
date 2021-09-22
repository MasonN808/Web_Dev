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
    from users.models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    return app

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
