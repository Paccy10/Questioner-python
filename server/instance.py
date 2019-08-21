from flask import Flask, Blueprint
from flask_restplus import Api
from config.environment import environment

api_blueprint = Blueprint('api_blueprint', __name__, url_prefix='/api/v1')
authorizations = {
    'Token Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}


class Server(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(
            api_blueprint,
            title='Questioner API',
            description='A crowd-source questions for a meetup API',
            security='Token Auth',
            doc=environment['swagger-url'],
            authorizations=authorizations
        )
        self.app.register_blueprint(api_blueprint)

    def run(self):
        self.app.run(
            debug=environment['debug'],
            port=environment['port']
        )


server = Server()
