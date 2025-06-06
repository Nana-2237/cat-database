
from marshmallow import Schema, fields

class CatSchema(Schema):
    CatID = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    Breed = fields.Str(required=True)
    Age = fields.Int(required=True)
    Gender = fields.Str(required=True, validate=lambda g: g in ('Male', 'Female'))
