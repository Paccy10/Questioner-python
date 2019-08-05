from flask import request
from flask_restplus import Resource
from server.instance import server
from models.user import User
from models.meetup import Meetup
from models.database import db
from schemas.meetup import MeetupSchema
from middlewares.token_required import token_required
from middlewares.check_role import check_role
from middlewares.validators import MeetupValidators
from helpers.responses import success_response

api = server.api


@api.route('/api/meetups')
class MeetupResource(Resource):
    @token_required
    @check_role
    def post(self):
        """"Endpoint to create a meetup"""

        request_data = request.get_json()
        validation_error = MeetupValidators.meetup_validator(request_data)

        if validation_error:
            return validation_error

        new_meetup = Meetup(**request_data)
        db.session.add(new_meetup)
        db.session.commit()
        meetup_schema = MeetupSchema(strict=True)
        success_response['message'] = 'Meetup successfully created'
        success_response['data'] = {
            'meetup': meetup_schema.dump(new_meetup).data
        }

        return success_response, 201

    def get(self):
        """"Endpoint to get all meetups"""

        meetups_schema = MeetupSchema(many=True, strict=True)
        meetups = meetups_schema.dump(Meetup.query.all()).data
        success_response['message'] = 'Meetups successfully fetched'
        success_response['data'] = {
            'meetups': meetups
        }

        return success_response, 200
