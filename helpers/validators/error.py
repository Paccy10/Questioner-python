from werkzeug.exceptions import BadRequest


def raise_validation_error(message):
    error = BadRequest()
    error.data = {
        'status': 'error',
        'message': message
    }
    raise error
