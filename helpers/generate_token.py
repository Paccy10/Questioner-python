import datetime
import os
import jwt


def generate_token(user: dict):
    """Generates the authentication token"""

    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
        'user': user
    }
    token = jwt.encode(
        payload,
        os.getenv('SECRET_KEY'),
        algorithm='HS256'
    )
    return token.decode('UTF-8')
