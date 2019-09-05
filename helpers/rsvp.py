from flask import request
from models.rsvp import Rsvp
from schemas.rsvp import RsvpSchema
from helpers.responses import success_response, error_response

EXCLUDED_FIELDS = ['deleted', 'deleted_at']


def update_rsvp_if_exists(meetup_id, request_data):
    rsvp = Rsvp.query.filter(
        Rsvp.user_id == request.decoded_token['user'],
        Rsvp.meetup_id == meetup_id).first()

    if rsvp:
        if request_data['response'].lower() == rsvp.response.lower():
            error_response['message'] = 'Sorry, you have already responded with that response'
            return error_response, 400

        rsvp.update(request_data)
        rsvp_schema = RsvpSchema(exclude=EXCLUDED_FIELDS)
        success_response['message'] = 'Rsvp successfully updated'
        success_response['data'] = {
            'rsvp': rsvp_schema.dump(rsvp)
        }
        return success_response, 200
