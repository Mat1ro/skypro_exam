class Config(object):
    """config for auto-deploy"""
    SQLALCHEMY_DATABASE_URI = "postgresql://$DB_USER:$DB_PASSWORD@pg/$DB_NAME"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
