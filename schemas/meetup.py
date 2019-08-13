from marshmallow import Schema, fields
from .base import BaseSchema


class MeetupSchema(BaseSchema):
    topic = fields.String(dump_only=True)
    location = fields.String(dump_only=True)
    happening_on = fields.DateTime(dump_only=True)
    images = fields.List(fields.String(), dump_only=True)
    tags = fields.List(fields.String(), dump_only=True)
