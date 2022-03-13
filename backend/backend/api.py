from flask_restx import Api

import settings

authorizations = {
    'clientToken': {
        'type': 'http',
        'scheme': 'basic'
    }
}


api = Api(version='0.1', title='Messenger Helpdesk', description='API for forwarding messages from Whatsapp to Matrix',
          url_scheme=settings.URL_SCHEME, authorizations=authorizations)


@api.errorhandler
def std_handler():
    return {'message': 'unexpected error'}, 500
