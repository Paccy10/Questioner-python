from flask_restplus import fields
from .collections import (user_namespace, meetup_namespace, question_namespace)

# swagger model defining signup fields
signup_model = user_namespace.model('Signup', {
    'firstname': fields.String(required=True, description='User firstname'),
    'lastname': fields.String(required=True, description='User lastname'),
    'othername': fields.String(required=False, description='User othername'),
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

# swagger model defining login fields
login_model = user_namespace.model('Login', {
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
    'body': fields.String(required=True, description='Question body')
})

# swagger model defining rsvp fields
rsvp_model = meetup_namespace.model('Rsvp', {
    'response': fields.String(required=True, description='RSVP response')
})

# swagger model defining comment fields
comment_model = question_namespace.model('Comment', {
    'body': fields.String(required=True, description='Comment body')
})

# swagger model defining images fields
images_model = meetup_namespace.model('Images', {
    'images': fields.List(fields.String(), required=True, description='Meetup images')
})

# swagger model defining tags fields
tags_model = meetup_namespace.model('Tags', {
    'tags': fields.List(fields.String(), required=True, description='Meetup Tags')
})
