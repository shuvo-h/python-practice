from marshmallow import fields, Schema

# bd data to serialized data
class UserSchema(Schema):
    id = fields.String()
    username = fields.String()
    email = fields.String()