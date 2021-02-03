import os
# import eventlet 
from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_login import LoginManager
# from flask_socketio import SocketIO, send
# from eventlet import wsgi
# from eventlet import websocket
from dotenv import load_dotenv

import models
from resources.users import user
from resources.user_profiles import profile
from resources.manager_user_profiles import manager_profile

load_dotenv()

DEBUG = True
PORT = 8000


app = Flask(__name__)

# TOGGLE THIS ON/OFF IF USING LOCALLY OR DEPLOYED!
app.config.update( 
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_SAMESITE='None'
)

login_manager = LoginManager()
app.secret_key =  os.getenv('SECRET_KEY')
login_manager.init_app(app)
# socketio = SocketIO(app, cors_allowed_origins='*', async_mode='eventlet')
# participants = set()

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

# @socketio.on('message')
# def handleMessage(msg):
#     print(msg)
#     send(msg, broadcast=True)
#     return None

# @websocket.WebSocketWSGI
# def handle(ws):
#     participants.add(ws)
#     try:
#         while True:
#             msg = ws.wait()
#             if m is None:
#                 break
#             for p in participants:
#                 p.send(msg)
    
#     finally:
#         participants.remove(ws)

# def dispatch(environ, start_repsonse):
#     if environ['PATH_INFO'] == '/chat':
#         return handle(environ, start_repsonse)
#     else:
#         start_repsonse('200 OK', [('content-type', 'text/html')])
#         html_path = os.path.join(os.path.dirname(__file__), 'websocket_chat.html')
#         return [open(html_path).read() % {'port': PORT}]

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
    # socketio.run(app)
    models.initialize()

if __name__ == '__main__':
    # socketio.run(app)
    # listener = eventlet.listen(('127.0.0.1', PORT))
    # wsgi.server(listener, dispatch)
    models.initialize()
    app.run(debug=DEBUG, port=PORT)