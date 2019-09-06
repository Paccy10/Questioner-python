from .error import raise_validation_error


class RsvpValidators:

    @classmethod
    def rsvp_validator(cls, data: dict):
        response = data.get('response')
        responses = ['yes', 'no', 'maybe']

        if not response or not response.strip():
            raise_validation_error('The response is required')

        if response.lower().strip() not in responses:
            raise_validation_error(
                "The response should be 'Yes', 'No' or 'Maybe'")
