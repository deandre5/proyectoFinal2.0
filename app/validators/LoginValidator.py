from marshmallow import Schema, fields, validate


class CreateLoginSchema(Schema):

    email = fields.Str(
        required=True, validate=validate.Email(), data_key='correo')
    password = fields.Str(required=True, validate=validate.Length(
        min=6, max=256), data_key='password')
