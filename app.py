import os
import helpers.base as helper
from flask import Flask, g
from flask_login import LoginManager
import models

# import eventlet
# from flask_socketio import SocketIO, send
# from eventlet import wsgi
# from eventlet import websocket

app = Flask(__name__)
login_manager = LoginManager()


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
    print('connected to db')


@app.after_request
def after_request(response):
    g.db.close()
    return response


@app.route('/')
def index():
    return 'Hello!'

# socketio = SocketIO(app, cors_allowed_origins='*', async_mode='eventlet')
# participants = set()

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

if 'ON_HEROKU' in os.environ:
    helper.set_session_cookies_true(app)
    print('on heroku!')
    # socketio.run(app)ƒ
    models.initialize()

if __name__ == '__main__':
    env_vars = helper.get_env_vars()
    app.secret_key = env_vars['secret']
    login_manager.init_app(app)
    cors = helper.set_cors()
    register_blueprint = helper.set_register_blueprint(app)
    # socketio.run(app)
    # listener = eventlet.listen(('127.0.0.1', PORT))
    # wsgi.server(listener, dispatch)    app.run(debug=DEBUG, port=PORT)
    models.initialize()
    app.run(debug=env_vars['debug'], port=env_vars['port'])
