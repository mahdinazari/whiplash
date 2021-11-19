import os


class Config:
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'ASDASDOWIQ!@&EQHC<XNYWGYW#!@')
    SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URL')
    INSTALLED_APPS = [
        'version',
    ]
    VERSION = 'v0.1.0'


class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')


class TestConfig(DevelopConfig):
    TESTING = True

