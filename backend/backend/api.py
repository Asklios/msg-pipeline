from flask_restx import Api

import settings

authorizations = {
    'clientToken': {
        'type': 'http',
        'scheme': 'basic'
    }
}


api = Api(version='1.0', title='MSG Pipeline', description='API for forwarding messages to a Websocket',
          url_scheme=settings.URL_SCHEME, authorizations=authorizations)


@api.errorhandler
def std_handler():
    return {'message': 'unexpected error'}, 500
