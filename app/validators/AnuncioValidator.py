from marshmallow import Schema, fields, validate
from  marshmallow.validate import Range

class CreateAnuncioSchema(Schema):

    titulo = fields.String(required=True, validate=validate.Length(
        min=1, max=256), data_key='titulo')

    descripcion = fields.String(required=True, validate=validate.Length(
        min=1, max=256), data_key='descripcion')
