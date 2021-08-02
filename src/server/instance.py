from flask import Flask
from flask_restx import Api

class Server():
    def __init__(self, ):
        self.application = Flask(__name__)
        self.api = Api(self.application,
            version = '1.0',
            title = 'Cartas para o Papai Noel',
            doc = '/docs'
        )

    def run(self, ):
        self.application.run(
            debug = True, port = 80, host='0.0.0.0'
        )

server = Server()