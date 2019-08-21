from flask_restplus import fields
from .collections import (user_namespace, meetup_namespace, question_namespace)

# swagger model defining user fields
user_model = user_namespace.model('User', {
    'firstname': fields.String(required=True, description='User firstname'),
    'lastname': fields.String(required=True, description='User lastname'),
    'othername': fields.String(required=False, description='User othername'),
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

# swagger model defining meetup fields
meetup_model = meetup_namespace.model('Meetup', {
    'topic': fields.String(required=True, description='Meetup topic'),
    'location': fields.String(required=True, description='Meetup location'),
    'happening_on': fields.String(required=False, description='Meetup happening_on'),
    'images': fields.List(fields.String(), required=False, description='Meetup images'),
    'tags': fields.List(fields.String(), required=False, description='Meetup tags')
})

# swagger model defining question fields
question_model = question_namespace.model('Question', {
    'title': fields.String(required=True, description='Question title'),
    'body': fields.String(required=True, description='Question body')
})
