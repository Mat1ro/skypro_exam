from flask_restx import Resource, Namespace
from flask import request

from app.dao.model.lecture import LectureSchema
from app.container import lecture_service

lecture_ns = Namespace('lectures')


@lecture_ns.route('/')
class LecturesView(Resource):
    def get(self):
        """get all lectures"""
        lectures = lecture_service.get_all()
        res = LectureSchema(many=True).dump(lectures)
        return res, 200

    def post(self):
        """create new lecture"""
        req_json = request.json
        lecture = lecture_service.create(req_json)
        return "status: ok", 201, {"location": f"/lectures/{lecture.id}"}


@lecture_ns.route('/<int:lid>')
class LectureView(Resource):
    def get(self, lid):
        """get lecture by id"""
        note = lecture_service.get_one(lid)
        res = LectureSchema().dump(note)
        return res, 200

    def put(self, lid):
        """update lecture by id"""
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = lid
        lecture_service.update(req_json)
        return "changed", 204

    def delete(self, lid):
        """delete lecture by id"""
        lecture_service.delete(lid)
        return "deleted", 204
