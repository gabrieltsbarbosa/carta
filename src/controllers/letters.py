from flask import Flask, request
from flask_restx import Api, Resource

from src.server.instance import server
from src.repositories.letterRepository import Repo

app, api = server.app, server.api


@api.route('/letters')
class Letters(Resource):
    @app.route('/letters/<int:id>', methods=['GET'])
    def getById(id):
        return Repo.get(id)

    def get(self, ):
        return Repo.get()

    def post(self, ):
        return Repo.insert(api.payload)

    @app.route('/letters/<int:id>', methods=['PUT'])
    def put(id):
        return Repo.update(id, api.payload)
    
    @app.route('/letters/<int:id>', methods=['DELETE'])
    def delete(id):
        return Repo.delete(id)