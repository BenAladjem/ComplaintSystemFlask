from flask import request
from flask_restful import Resource
from menagers.complainer import ComplainerManager
from schemas.requests.auth import RegisterSchemaRequest
from utils.decorators import validate_schema

class RegisterResource(Resource):
    @validate_schema(RegisterSchemaRequest)
    def post(self):
        data = request.get_json()
        token = ComplainerManager.register(data)
        return {"token": token}, 201

