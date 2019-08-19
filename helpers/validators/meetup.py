import datetime
from .error import raise_validation_error


class MeetupValidators:

    @classmethod
    def meetup_validator(cls, data: dict):
        topic = data.get('topic')
        location = data.get('location')
        happening_on = data.get('happening_on')

        if not topic or not topic.strip():
            raise_validation_error('The topic is required')

        if not location or not location.strip():
            raise_validation_error('The location is required')

        if not happening_on or not happening_on.strip():
            raise_validation_error('The happening_on date is required')

        try:
            datetime.datetime.strptime(happening_on, '%Y-%m-%d')
        except ValueError:
            raise_validation_error('Invalid date format. It should be like YYYY-MM-DD')

        if datetime.datetime.strptime(happening_on, '%Y-%m-%d').date() < datetime.date.today():
            message = 'Invalid date. The date should be greater or equal to today\'s date'
            raise_validation_error(message)
