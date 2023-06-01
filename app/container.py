from app.dao.lecture import LectureDAO
from app.service.lecture import LectureService
from app.setup_db import db

# Установка DAO и service
lecture_dao = LectureDAO(session=db.session)

lecture_service = LectureService(dao=lecture_dao)


