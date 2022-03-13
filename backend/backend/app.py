import json

from flask import Flask, Blueprint

from settings import *
from api import api
from endpoint import namespace
from websocket import socket

app = Flask(__name__)

app.config['SERVER_NAME'] = SERVER_NAME
app.config['SWAGGER_UI_DOC_EXPANSION'] = RESTPLUS_SWAGGER_EXPANSION
app.config['RESTPLUS_VALIDATE'] = RESTPLUS_VAL
app.config['RESTPLUS_MASK_SWAGGER'] = RESTPLUS_MASK_SWAGGER

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api.init_app(blueprint)
api.add_namespace(namespace)
app.register_blueprint(blueprint)
socket.init_app(app)


if __name__ == '__main__':
    if EXPORT_SWAGGER_FILE:
        with app.app_context():
            print(json.dumps(api.__schema__))
            exit()
    app.run()

application = app
