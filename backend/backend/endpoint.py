from flask import request
from flask_restx import Resource, fields

import websocket
import settings
from api import api

namespace = api.namespace('messages', description='Message Input')


event_message = api.model(
    'EventMessage',
    {
        "room": fields.String(required=True, description='A room ID'),
        "event_id": fields.String(required=True, description='A message ID'),
        "message": fields.String(required=True, description='The message body'),
        "reply": fields.String(description='An optional reply event')
    }
)

event_delete = api.model(
    'EventDelete',
    {
        "room": fields.String(required=True, description='A room ID'),
        "event_id": fields.String(required=True, description='Message event id')
    }
)


def check_token(func):
    def inner(self, **args):
        token = request.headers.get('Authorization')

        if token is None:
            return {'error': 'missing token'}, 401

        if token != settings.RECEIVE_TOKEN:
            return {'error': 'token not valid'}, 401

        return func(self, **args)
    return inner


@namespace.route('/', strict_slashes=False)
class Message(Resource):

    @api.doc(security='clientToken')
    @api.expect(event_message, validate=True)
    @check_token
    def post(self):
        j = request.json
        j['type'] = "message"
        websocket.send_json(j)
        return {"message": "success"}


@namespace.route('/delete')
class Message(Resource):

    @api.doc(security='clientToken')
    @api.expect(event_delete, validate=True)
    @check_token
    def post(self):
        j = request.json
        j['type'] = "delete"
        websocket.send_json(j)
        return {"message": "success"}


@namespace.route('/health')
class Health(Resource):
    
    @staticmethod
    def get():
        return {"message": "healthy"}, 200
