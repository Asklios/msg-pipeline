from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from app import application
from settings import *


print('----STARTUP----')
http_server = WSGIServer(('', PORT), application, handler_class=WebSocketHandler)
http_server.serve_forever()
