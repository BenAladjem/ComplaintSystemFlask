from flask import request
from flask_restful import Resource
from menagers.complainer import ComplainerManager


class RegisterResource(Resource):

    def post(self):
        data = request.get_json()
        token = ComplainerManager.register(self, data)
        return {"token": token}, 201

