import datetime
from sqlalchemy.dialects import postgresql
from .database import db


class BaseModel(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    deleted = db.Column(db.Boolean, default=False, nullable=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    def save(self):
        self.created_at = datetime.datetime.utcnow()
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.updated_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        self.deleted = True
        self.deleted_at = datetime.datetime.utcnow()
        db.session.add(self)
        db.session.commit()
