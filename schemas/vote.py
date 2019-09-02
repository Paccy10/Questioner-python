from marshmallow import Schema, fields
from .base import BaseSchema


class VoteSchema(BaseSchema):
    user_id = fields.Integer(dump_only=True)
    question_id = fields.Integer(dump_only=True)
    upvote = fields.Boolean(dump_only=True)
    downvote = fields.Boolean(dump_only=True)
