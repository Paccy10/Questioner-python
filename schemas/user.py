from marshmallow import Schema, fields
from .base import BaseSchema


class UserSchema(BaseSchema):
    firstname = fields.String(dump_only=True)
    lastname = fields.String(dump_only=True)
    othername = fields.String(dump_only=True)
    email = fields.String(dump_only=True)
    password = fields.String(dump_only=True)
    is_admin = fields.Boolean(dump_only=True)
