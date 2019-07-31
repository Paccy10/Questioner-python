import datetime
import os
import jwt


def generate_token(user_id: int):
    """Generates the authentication token"""

    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
        'user': user_id
    }
    token = jwt.encode(
        payload,
        os.getenv('SECRET_KEY'),
        algorithm='HS256'
    )
    return token.decode('UTF-8')
