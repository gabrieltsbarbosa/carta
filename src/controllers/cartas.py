from flask import Flask, request
from flask_restx import Api, Resource

from src.server.instance import server

app, api = server.app, server.api

cartas_db = [
]

@api.route('/cartas')
class Cartas(Resource):
    def get(self, ):
        i = request.args.get('id')
        print('\n\n\n\n\n\n')
        print(i)
        if i == None:
            return cartas_db
        else:
            return cartas_db[int(i)]

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
        return response, 201

    def put(self, ):
        response = api.payload
        id = int(request.args.get('id'))
        carta = cartas_db[id]
        carta[id][response['item']] = response['content']
        return response, 200
        
    def delete(self, ):
        try:
            response = api.payload
            cartas_db.pop(int(response['id']))
            return response, 200

        except:
            return "Error", 404