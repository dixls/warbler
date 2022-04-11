
import flask_sqlalchemy


class Config:
    """
    Base configuration class. Contains default config settings.
    """

    SQLALCHEMY_DATABASE_URI = 'postgresql:///warbler'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    FLASK_ENV = 'development'
    WTF_CSRF_ENABLED = True


class DevelopmentConfig(Config):
    SECRET_KEY = "I'LL NEVER TELL!!"
    TESTING = False


class TestingConfig(Config):
    WTF_CSRF_ENABLED = False
    TESTING = True
    FLASK_ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'postgresql:///warbler-test'
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DEBUG_TB_ENABLED = False
    SECRET_KEY = "Still bad!"
