# import eventlet
# from flask_socketio import SocketIO, send
# from eventlet import wsgi
# from eventlet import websocket

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


# main
# socketio.run(app)
# listener = eventlet.listen(('127.0.0.1', PORT))
# wsgi.server(listener, dispatch)    app.run(debug=DEBUG, port=PORT)
