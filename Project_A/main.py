
from flask import Blueprint, render_template, flash

from __init__ import create_app, db


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
    db.create_all(app=create_app())  # create the SQLite database
    app.run(debug=True)  # run the flask app on debug mode
