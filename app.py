from flask import Flask, jsonify, g
from flask_cors import CORS
# from flask_login import LoginManager

import models
from resources.users import user
from resources.user_profiles import profile

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

CORS(profile, origins=['*'], supports_credentials=True)
CORS(user, origins=['*'], supports_credentials=True)

app.register_blueprint(profile, url_prefix='/profile')
app.register_blueprint(user, url_prefix='/users')

@app.route('/')
def index():
    return 'Hello!'

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)