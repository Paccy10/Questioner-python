from marshmallow import Schema, fields
from .base import BaseSchema
from .user import UserSchema


class CommentSchema(BaseSchema):
    body = fields.String(dump_only=True)
    question_id = fields.Integer(dump_only=True)
    commentor = fields.Nested(
        UserSchema, only=['id', 'firstname', 'lastname', 'othername', 'email'])
