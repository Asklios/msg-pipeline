import os

PORT = os.environ.get('PORT', 5000)
SERVER_NAME = os.environ.get('SERVER_NAME', f'localhost:{PORT}')
URL_SCHEME = os.environ.get('URL_SCHEME', 'http')

RESTPLUS_SWAGGER_EXPANSION = os.environ.get('RESTPLUS_SWAGGER_EXPANSION', 'list')
RESTPLUS_VAL = os.environ.get('RESTPLUS_VAL', True)
RESTPLUS_MASK_SWAGGER = os.environ.get('RESTPLUS_MASK_SWAGGER', False)

RECEIVE_TOKEN = os.environ.get('CLIENT_TOKEN', 'test_token')
SEND_TOKEN = os.environ.get('CLIENT_TOKEN', 'test_token')

EXPORT_SWAGGER_FILE = os.environ.get('EXPORT_SWAGGER_FILE') is not None
