from marshmallow import fields, Schema, validate


class RegisterSchemaRequest(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=1, max=20))
    first_name = fields.Str(required=True, validate=validate.Length(min=1, max=20))
    last_name = fields.Str(required=True, validate=validate.Length(min=1, max=20))
    phone = fields.Str(required=True, validate=validate.Length(min=14, max=14))
