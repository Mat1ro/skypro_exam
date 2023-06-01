from app.dao.lecture import LectureDAO


class LectureService:
    def __init__(self, dao: LectureDAO):
        self.dao = dao

    def get_one(self, lid):
        """get lecture by id"""
        return self.dao.get_one(lid)

    def get_all(self):
        """get all lectures"""
        return self.dao.get_all()

    def create(self, lecture_data):
        """create new lecture"""
        return self.dao.create(lecture_data)

    def update(self, lecture_data):
        """update lecture"""
        self.dao.update(lecture_data)
        return self.dao

    def delete(self, lid):
        """delete lecture"""
        self.dao.delete(lid)
