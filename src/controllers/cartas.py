from flask import Flask, request
from flask_restx import Api, Resource

from src.server.instance import server
from src.repositories.cardRepository import Repo

app, api = server.app, server.api


@api.route('/cartas')
class Cartas(Resource):
    @app.route('/cartas/<int:id>', methods=['GET'])
    def getById(id):
        return Repo.catch(id)

    def get(self, ):
        return Repo.catch()

    def post(self, ):
        return Repo.insert(api.payload)

    @app.route('/cartas/<int:id>', methods=['PUT'])
    def put(id):
        return Repo.update(id, api.payload)
    
    @app.route('/cartas/<int:id>', methods=['DELETE'])
    def delete(id):
        return Repo.delete(id)