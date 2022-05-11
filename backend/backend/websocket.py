from flask import request
from flask_socketio import SocketIO
from engineio.async_drivers import gevent

import settings

socket = SocketIO(None, cors_allowed_origins='*', async_mode='gevent')

ws_clients: [str] = []


@socket.on('connect')
def connect(auth):
    print('Client connected')
    if auth is None:
        return False
    if not isinstance(auth, str):
        return False
    if auth == settings.SEND_TOKEN:
        global ws_clients
        ws_clients.append(request.sid)
        print(f'Client authenticated {request.sid}')
        print(f'{len(ws_clients)} clients connected')
    else:
        return False


@socket.on('disconnect')
def disconnect():
    global ws_clients
    try:
        ws_clients.remove(request.sid)
    except ValueError:
        pass
    print('Client disconnected')


def send_json(json):
    socket.send(json)
