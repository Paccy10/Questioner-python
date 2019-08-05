from sqlalchemy.dialects import postgresql
from .database import db
from .base import BaseModel


class Meetup(BaseModel):

    __tablename__ = 'meetups'

    topic = db.Column(db.String(250), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    happening_on = db.Column(db.DateTime, nullable=False)
    images = db.Column(postgresql.ARRAY(db.String), nullable=True)
    tags = db.Column(postgresql.ARRAY(db.String(100)), nullable=True)
