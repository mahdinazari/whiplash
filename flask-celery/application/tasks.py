from .config import Config
from .celery import celery


# Create celery instance
#celery = Celery(
#    'tasks',
#    backend=Config.CELERY_BACKEND_URL,
#    broker=Config.CELERY_BROKER_URL,
#)
#celery = Celery('tasks')
#celery.config_from_object('celery_config')


@celery.task
def add(x, y):
    return x + y

@celery.task
def mul(x, y):
    return x * y

