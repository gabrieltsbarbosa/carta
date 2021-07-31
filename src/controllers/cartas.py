from flask import Flask, request
from flask_restx import Api, Resource

from src.server.instance import server

app, api = server.app, server.api

cartas_db = {}

@api.route('/cartas')
class Cartas(Resource):
    @app.route('/cartas/<int:id>', methods=['GET'])
    def getById(id):
        for i in cartas_db:
            if i == id:
                return cartas_db[id], 200

        return "", 404

    def get(self, ):
        cartas = []
        for i in cartas_db:
            cartas.append(cartas_db[i])
        return cartas

    def post(self, ):
        response = api.payload
        id = len(cartas_db) + 1
        carta = {
            id:{
                'id': id,
                'nome': response['nome'],
                'endereco': response['endereco'],
                'texto':response['texto']
            }
        }
        cartas_db.update(carta)
        return carta[id], 201

    @app.route('/cartas/<int:id>', methods=['PUT'])
    def put(id):
        response = api.payload
        carta = cartas_db[id]
        carta[id][response['item']] = response['content']
        return response, 200
    
    @app.route('/cartas/<int:id>', methods=['DELETE'])
    def delete(id):
        try:
            response = api.payload
            cartas_db.pop(int(id))
            return response, 200

        except:
            return "Error", 404