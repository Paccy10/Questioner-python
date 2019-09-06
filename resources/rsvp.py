from flask import request
from flask_restplus import Resource
from models.rsvp import Rsvp
from schemas.rsvp import RsvpSchema
from middlewares.token_required import token_required
from helpers.swagger.collections import meetup_namespace
from helpers.swagger.models import rsvp_model
from helpers.validators.rsvp import RsvpValidators
from helpers.responses import success_response, error_response
from helpers.rsvp import update_rsvp_if_exists
from helpers.meetup import get_meetup
from helpers.request_data_strip import request_data_strip

EXCLUDED_FIELDS = ['deleted', 'deleted_at']


@meetup_namespace.route('/<int:meetup_id>/rsvps')
class RsvpResource(Resource):
    @token_required
    @meetup_namespace.expect(rsvp_model)
    def post(self, meetup_id):
        """Endpoint to create an rsvp"""

        meetup = get_meetup(meetup_id)

        if not meetup:
            error_response['message'] = 'Meetup not found'
            return error_response, 404

        request_data = request.get_json()
        RsvpValidators.rsvp_validator(request_data)

        request_data = request_data_strip(request_data)

        request_data.update(
            {
                'user_id': request.decoded_token['user'],
                'meetup_id': meetup_id
            }
        )
        updated_rsvp = update_rsvp_if_exists(meetup_id, request_data)
        if updated_rsvp:
            return updated_rsvp

        new_rsvp = Rsvp(**request_data)
        new_rsvp.save()
        rsvp_schema = RsvpSchema(exclude=EXCLUDED_FIELDS)
        success_response['message'] = 'Rsvp successfully created'
        success_response['data'] = {
            'rsvp': rsvp_schema.dump(new_rsvp)
        }

        return success_response, 201

    @token_required
    def get(self, meetup_id):
        """"Endpoint to get all rsvps"""

        meetup = get_meetup(meetup_id)

        if not meetup:
            error_response['message'] = 'Meetup not found'
            return error_response, 404

        rsvps_schema = RsvpSchema(many=True, exclude=EXCLUDED_FIELDS)
        rsvps = rsvps_schema.dump(
            Rsvp.query.filter(Rsvp.meetup_id == meetup_id, Rsvp.deleted == False))
        success_response['message'] = 'Rsvps successfully fetched'
        success_response['data'] = {
            'rsvps': rsvps
        }

        return success_response, 200
