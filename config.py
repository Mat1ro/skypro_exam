class Config(object):
    """config flask app"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///lectures.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
