from models.meetup import Meetup
from schemas.meetup import MeetupSchema

EXCLUDED_FIELDS = ['deleted', 'deleted_at']


def get_meetup(meetup_id):
    meetup_schema = MeetupSchema(exclude=EXCLUDED_FIELDS)
    meetup = meetup_schema.dump(
        Meetup.query.filter_by(id=meetup_id, deleted=False).first())

    return meetup
