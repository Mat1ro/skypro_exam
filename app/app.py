from flask import Flask

from flask_restx import Api

from config import Config
from app.setup_db import db
from app.views.lecture import lecture_ns


def create_app(config_object):
    """Creating flask app"""
    app = Flask(__name__)
    app.config.from_object(config_object)
    db.init_app(app)
    register_extensions(app)
    return app


def register_extensions(app):
    """Register API"""
    api = Api(app)
    api.add_namespace(lecture_ns)


app = create_app(Config())

# Creating database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
