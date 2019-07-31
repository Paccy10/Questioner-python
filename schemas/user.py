from flask_marshmallow import Marshmallow
from server.instance import server

app = server.app
marshmallow = Marshmallow(app)


class UserSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'firstname', 'lastname', 'othername', 'email', 'password',
                  'is_admin', 'created_at', 'updated_at')
