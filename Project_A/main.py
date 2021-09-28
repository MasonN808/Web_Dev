from flask import Blueprint, render_template
from __init__ import create_app, db
from flask_login import login_required, current_user
# Main blueprint
main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


# @main.route('/login')
# def login():
#     return render_template('login.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name = current_user.name)


# @main.route('/signup')
# def signup():
#     return render_template('signup.html')


# make app

app = create_app()

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, debug=True)
    db.create_all(app=create_app())  # create the SQLite database
    app.run(debug=True)  # run the flask app on debug mode
