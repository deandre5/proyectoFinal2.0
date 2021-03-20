from marshmallow import Schema, fields, validate


class CreateImcSchema(Schema):

    peso = fields.String(required=True, validate=validate.Length(
        min=2, max=3), data_key='peso')

    altura = fields.String(
        required=True, validate=validate.Length(min=2, max=3), data_key='altura')
