from datetime import datetime
from flask import request
from flask_restplus import Resource
from server.instance import server
from models.user import User
from models.meetup import Meetup
from models.database import db
from schemas.meetup import MeetupSchema
from middlewares.token_required import token_required
from middlewares.check_role import check_role
from middlewares.validators.meetup import MeetupValidators
from helpers.responses import success_response, error_response

api = server.api
EXCLUDED_FIELDS = ['deleted', 'deleted_at']


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
        new_meetup.save()
        meetup_schema = MeetupSchema(strict=True, exclude=EXCLUDED_FIELDS)
        success_response['message'] = 'Meetup successfully created'
        success_response['data'] = {
            'meetup': meetup_schema.dump(new_meetup).data
        }

        return success_response, 201

    def get(self):
        """"Endpoint to get all meetups"""

        meetups_schema = MeetupSchema(many=True, strict=True,
                                      exclude=EXCLUDED_FIELDS)
        meetups = meetups_schema.dump(
            Meetup.query.filter_by(deleted=False)).data
        success_response['message'] = 'Meetups successfully fetched'
        success_response['data'] = {
            'meetups': meetups
        }

        return success_response, 200


@api.route('/api/meetups/<int:meetup_id>')
class SingleMeetupResource(Resource):
    def get(self, meetup_id):
        """"Endpoint to get a single meetup"""

        meetup_schema = MeetupSchema(strict=True, exclude=EXCLUDED_FIELDS)
        meetup = meetup_schema.dump(
            Meetup.query.filter_by(id=meetup_id, deleted=False).first()).data
        if not meetup:
            error_response['message'] = 'Meetup not found'
            return error_response, 404
        success_response['message'] = 'Meetup successfully fetched'
        success_response['data'] = {
            'meetup': meetup
        }

        return success_response, 200

    @token_required
    @check_role
    def put(self, meetup_id):
        """"Endpoint to update a meetup"""

        meetup = Meetup.query.filter_by(id=meetup_id, deleted=False).first()
        if not meetup:
            error_response['message'] = 'Meetup not found'
            return error_response, 404

        request_data = request.get_json()
        validation_error = MeetupValidators.meetup_validator(request_data)

        if validation_error:
            return validation_error

        meetup_schema = MeetupSchema(strict=True, exclude=EXCLUDED_FIELDS)
        meetup.update(request_data)
        success_response['message'] = 'Meetup successfully updated'
        success_response['data'] = {
            'meetup': meetup_schema.dump(meetup).data
        }

        return success_response, 200

    @token_required
    @check_role
    def delete(self, meetup_id):
        """"Endpoint to delete a meetup"""

        meetup = Meetup.query.filter_by(id=meetup_id, deleted=False).first()
        if not meetup:
            error_response['message'] = 'Meetup not found'
            return error_response, 404

        meetup.delete()
        meetup_schema = MeetupSchema(strict=True)
        success_response['message'] = 'Meetup successfully deleted'
        success_response['data'] = {
            'meetup': meetup_schema.dump(meetup).data
        }

        return success_response, 200


@api.route('/api/meetups/upcoming')
class UpcomingMeetupsResource(Resource):
    def get(self):
        """"Endpoint to get all upcoming meetups"""

        meetups_schema = MeetupSchema(many=True, strict=True,
                                      exclude=EXCLUDED_FIELDS)
        meetups = meetups_schema.dump(
            Meetup.query.filter(Meetup.happening_on >= datetime.now(),
                                Meetup.deleted == False)).data

        success_response['message'] = 'Upcoming meetups successfully fetched'
        success_response['data'] = {
            'meetups': meetups
        }

        return success_response, 200
