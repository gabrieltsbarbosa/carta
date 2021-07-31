import re
from flask import Flask
from flask_restx import Api, Resource

from src.server.instance import server

app, api = server.app, server.api

cartas_db = [
]

@api.route('/cartas')
class Cartas(Resource):
    def get(self, ):
        return cartas_db

    def post(self, ):
        response = api.payload
        id = len(cartas_db)
        carta = {
            id:{
                'nome': response['nome'],
                'endereco': response['endereco'],
                'texto':response['texto']
            }
        }
        cartas_db.append(carta)
        return response, 200