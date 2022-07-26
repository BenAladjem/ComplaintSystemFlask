from marshmallow import fields, Schema, validate
from schemas.requests.base import AuthBase


class RegisterSchemaRequest(AuthBase):

    first_name = fields.Str(required=True, validate=validate.Length(min=1, max=20))
    last_name = fields.Str(required=True, validate=validate.Length(min=1, max=20))
    phone = fields.Str(required=True, validate=validate.Length(min=14, max=14))


class LoginSchemaRequest(AuthBase):
    pass




