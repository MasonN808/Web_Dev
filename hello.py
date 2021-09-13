import os
from flask import Flask, render_template
from flask.ext.bootsrap import Bootstrap
import os

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

# @app.route("/")
# def index():
#     return render_template("index.html", message="Hello Flask!")

bootstrap = Bootstrap(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000, debug=True)
    # app.run(debug = True)