from marshmallow import Schema, fields
from .base import BaseSchema
from .user import UserSchema
from .meetup import MeetupSchema


class QuestionSchema(BaseSchema):
    title = fields.String(dump_only=True)
    body = fields.String(dump_only=True)
    meetup_id = fields.Integer(dump_only=True)
    author = fields.Nested(
        UserSchema, only=['id', 'firstname', 'lastname', 'othername', 'email'])
