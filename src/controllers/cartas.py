from flask import Flask, request
from flask_restx import Api, Resource

from src.server.instance import server
from src.repositories.cardRepository import Repo

application, api = server.application, server.api


@api.route('/cartas')
class Cartas(Resource):
    @application.route('/cartas/<int:id>', methods=['GET'])
    def getById(id):
        return Repo.get(id)

    def get(self, ):
        return Repo.get()

    def post(self, ):
        return Repo.insert(api.payload)

    @application.route('/cartas/<int:id>', methods=['PUT'])
    def put(id):
        return Repo.update(id, api.payload)
    
    @application.route('/cartas/<int:id>', methods=['DELETE'])
    def delete(id):
        return Repo.delete(id)

    @application.route('/', methods=['GET', 'POST'])
    def healthCheck():
        return 'healthCheck', 200