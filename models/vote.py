from .database import db
from .base import BaseModel


class Vote(BaseModel):

    __tablename__ = 'votes'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey(
        'questions.id'), nullable=False)
    upvote = db.Column(db.Boolean, default=False, nullable=False)
    downvote = db.Column(db.Boolean, default=False, nullable=False)
