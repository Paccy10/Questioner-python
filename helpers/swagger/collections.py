from flask_restplus import fields
from server.instance import api


# Remove default namespace
api.namespaces.clear()

user_namespace = api.namespace(
    'Users',
    description='A collection of User related endpoints',
    path='/auth'
)

meetup_namespace = api.namespace(
    'Meetups',
    description='A collection of Meetup related endpoints',
    path='/meetups'
)

question_namespace = api.namespace(
    'Questions',
    description='A collection of Question related endpoints'
)
