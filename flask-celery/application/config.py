import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI',
        'postgresql://postgres:postgres@localhost/practice'
    )

    # Registration apps
    REGISTERED_APP = [
        'index',
    ]

    # Celery configuration
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_BACKEND_URL = 'db+postgresql://postgres:postgres@localhost/practice'

