from marshmallow import Schema, fields


class UserSchema(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    name = fields.Str(required=True)
    surname = fields.Str(required=True)
    favorite_genre = fields.Str(required=True)
    role = fields.Str(required=True)
