from menagers.auth import AuthManager
from werkzeug.security import generate_password_hash
from  models.user import ComplainerModel

class ComplainerManager:
    @staticmethod
    def register(self, complainer_data):
        complainer_data["password"] = generate_password_hash(complainer_data["password"])
        user = ComplainerModel(**data)
        db.session.add(user)
        db.session.commit()
        return AuthManager.encode_token(user)