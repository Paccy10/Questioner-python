from flask import Flask
from flask_restplus import Api
from config.environment import environment


class Server(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(
            self.app,
            version='1.0',
            title='Sample Book API',
            description='A simple Book API',
            doc=environment['swagger-url']
        )

    def run(self):
        self.app.run(
            debug=environment['debug'],
            port=environment['port']
        )


server = Server()
