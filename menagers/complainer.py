from menagers.auth import AuthManager
from werkzeug.security import generate_password_hash
from models.user import ComplainerModel

from db import db


class ComplainerManager:
    @staticmethod
    def register(complainer_data):
        complainer_data["password"] = generate_password_hash(complainer_data["password"])
        user = ComplainerModel(**complainer_data)
        db.session.add(user)
        db.session.commit()
        return AuthManager.encode_token(self, user)



