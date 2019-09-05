from marshmallow import Schema, fields
from .base import BaseSchema
from .user import UserSchema
from .meetup import MeetupSchema


class RsvpSchema(BaseSchema):
    response = fields.String(dump_only=True)
    meetup_id = fields.Integer(dump_only=True)
    user = fields.Nested(
        UserSchema, only=['id', 'firstname', 'lastname', 'othername', 'email'])
    meetup = fields.Nested(
        MeetupSchema, only=['id', 'topic', 'location', 'happening_on'])
