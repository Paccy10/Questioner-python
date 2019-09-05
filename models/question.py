from .database import db
from .base import BaseModel


class Question(BaseModel):

    __tablename__ = 'questions'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    meetup_id = db.Column(db.Integer, db.ForeignKey(
        'meetups.id'), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.relationship('User', backref='author', lazy=True)
