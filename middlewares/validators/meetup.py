import datetime
from helpers.responses import error_response


class MeetupValidators:

    @classmethod
    def meetup_validator(cls, data: dict):
        topic = data.get('topic')
        location = data.get('location')
        happening_on = data.get('happening_on')

        if not topic or not topic.strip():
            error_response['message'] = 'The topic is required'
            return error_response, 400

        if not location or not location.strip():
            error_response['message'] = 'The location is required'
            return error_response, 400

        if not happening_on or not happening_on.strip():
            error_response['message'] = 'The happening_on date is required'
            return error_response, 400

        try:
            datetime.datetime.strptime(happening_on, '%Y-%m-%d')
            print(datetime.date.today())
        except ValueError:
            error_response['message'] = 'Invalid date format. It should be like YYYY-MM-DD'
            return error_response, 400

        if datetime.datetime.strptime(happening_on, '%Y-%m-%d').date() < datetime.date.today():
            message = 'Invalid date. The date should be greater or equal to today\'s date'
            error_response['message'] = message
            return error_response, 400
