from .database import db
from .base import BaseModel


class Comment(BaseModel):

    __tablename__ = 'comments'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey(
        'questions.id'), nullable=False)
    body = db.Column(db.Text, nullable=False)
    commentor = db.relationship('User', backref='commentor', lazy=True)
