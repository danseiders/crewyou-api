from flask import Flask, jsonify, g
# from flask_login import LoginManager

import models
# from resources.users import users

DEBUG = True
PORT = 8000

app = Flask(__name__)

# app.secret_key = 'thisisasecretasdlfjkas'
# login_manager = LoginManager()

@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route('/')
def index():
    return 'Hello!'

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)