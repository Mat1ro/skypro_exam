from datetime import datetime

from marshmallow import Schema, fields

from app.setup_db import db


class Lecture(db.Model):
    """Lecture table"""
    __tablename__ = 'lecture'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    teacher = db.Column(db.Text(100))
    classroom = db.Column(db.Integer)


class LectureSchema(Schema):
    """Schema of the lecture table"""
    id = fields.Integer()
    title = fields.String()
    date = fields.DateTime()
    teacher = fields.String()
    classroom = fields.Integer()
