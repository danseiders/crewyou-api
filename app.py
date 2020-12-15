import os
from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_login import LoginManager
from flask_socketio import SocketIO, send
from dotenv import load_dotenv

import models
from resources.users import user
from resources.user_profiles import profile
from resources.manager_user_profiles import manager_profile

load_dotenv()

DEBUG = True
PORT = 8000
# REDIS_URL = os.environ['REDIS_URL']
# REDIS_CHAN = 'chat'

app = Flask(__name__)

app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_SAMESITE='None'
)

login_manager = LoginManager()
app.secret_key =  os.getenv('SECRET_KEY')
login_manager.init_app(app)
socketio = SocketIO(app, cors_allowed_origins='*')

@login_manager.user_loader
def load_user(user_id):
    try:
        return models.Users.get(models.Users.id == user_id)
    except models.DoesNotExist:
        return None

@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

@socketio.on('message')
def handleMessage(msg):
    print(msg)
    send(msg, broadcast=True)
    return None

CORS(profile, origins=['*'], supports_credentials=True)
CORS(user, origins=['*'], supports_credentials=True)
CORS(manager_profile, origins=['*'], supports_credentials=True)

app.register_blueprint(profile, url_prefix='/profile')
app.register_blueprint(user, url_prefix='/users')
app.register_blueprint(manager_profile, url_prefix='/managers')

@app.route('/')
def index():
    return 'Hello!'

if 'ON_HEROKU' in os.environ:
    print('on heroku!')
    models.initialize()
    # socketio.run(app)

if __name__ == '__main__':
    models.initialize()
    # socketio.run(app)
    app.run(debug=DEBUG, port=PORT)