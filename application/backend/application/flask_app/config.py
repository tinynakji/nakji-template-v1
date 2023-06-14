import os


basedir = os.path.abspath(os.path.dirname(__file__))

from flask_app.db.database import get_database_url

class ConfigBase:
    AUTHENTICATION_ENABLED = True
    DEBUG = True
    SECRET_KEY = None
    DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True


class TestConfig(ConfigBase):
    AUTHENTICATION_ENABLED = False
    # DATABASE_URI = 'sqlite:///' + TEST_DB_FILE_NAME
    DATABASE_URI = get_database_url(testing=True)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(ConfigBase):
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DATABASE_URI = os.environ.get('DATABASE_URI')\
        or get_database_url()
    SQLALCHEMY_TRACK_MODIFICATIONS = False