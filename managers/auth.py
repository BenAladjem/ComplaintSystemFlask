import jwt

from datetime import datetime, timedelta
from decouple import config
from werkzeug.exceptions import Unauthorized


class AuthManager:
    @staticmethod
    def encode_token(user):
        payload = {"sub": user.id, "exp": datetime.utcnow() + timedelta(days=2), "type":user.__class__.__name__}
        return jwt.encode(payload, key=config("JWT_SECRET"), algorithm="HS256")

