from flask_marshmallow import Marshmallow
from server.instance import server

app = server.app
marshmallow = Marshmallow(app)


class MeetupSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'topic', 'location', 'happening_on',
                  'images', 'tags', 'created_at', 'updated_at', 'deleted', 'deleted_at')
