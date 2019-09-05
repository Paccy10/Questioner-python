from .database import db
from .base import BaseModel


class Rsvp(BaseModel):

    __tablename__ = 'rsvps'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    meetup_id = db.Column(db.Integer, db.ForeignKey(
        'meetups.id'), nullable=False)
    response = db.Column(db.String(200), nullable=False)
    user = db.relationship('User', backref='user', lazy=True)
    meetup = db.relationship('Meetup', backref='meetup', lazy=True)
