class Config(object):
    """config for local deploy"""
    SQLALCHEMY_DATABASE_URI = "postgresql://exam:exam_pass@pg/exam"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
