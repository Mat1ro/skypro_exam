from app.dao.model.lecture import Lecture
from app.setup_db import db


class LectureDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, lid):
        """Get lecture by id"""
        return self.session.query(Lecture).get(lid)

    def get_all(self):
        """Get all lectures"""
        return self.session.query(Lecture).all()

    def create(self, lecture_data):
        """Create new lecture"""
        lecture = Lecture(**lecture_data)
        self.session.add(lecture)
        self.session.commit()
        return lecture

    def delete(self, lid):
        """delete lecture by id"""
        lecture = self.get_one(lid)
        self.session.delete(lecture)
        self.session.commit()

    def update(self, lecture_data):
        """update lecture by id"""
        lecture = self.get_one(lecture_data.get("id"))
        lecture.title = lecture_data.get("title")
        lecture.date = lecture_data.get("date")
        lecture.teacher = lecture_data.get("teacher")
        lecture.classroom = lecture_data.get("classroom")

        self.session.add(lecture)
        self.session.commit()

