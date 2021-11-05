# from celery import Celery

from application.config import Config
from application.celery import celery
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


# commented because set config from config file
#app = Celery(
#    'tasks',
#    backend=Config.CELERY_BACKEND_URL,
#    broker=Config.CELERY_BROKER_URL,
#)

# commened because app moved to celery.py
#app = Celery('tasks')
#app.config_from_object('application.celery_config')


@celery.task(track_started=True)
def add(x, y):
    logger.info("Add task has been started")
    return x + y

@celery.task
def mul(x, y):
    logger.info("Mul task has been started")
    return x / y

@celery.task(bind=True, kwargs={'max_retries': 3}, autoretry_for=(ZeroDivisionError, ), retry_backoff=True,)
def say_hello(self, name):
    logger.info("Say Hello task has been started")
    if not self.request.retries > 0:
        i = 0

    else:
        i = 1

    try:
        1 / i
        print("************************hello %s" %name)
        return({'name': name})

    except Exception as exc:
        print('*************retry****************')
        self.retry(countdown=5, exc=exc)

@celery.task
def hello(name):
    print("Run Period Task Hello %s" %name)

celery.conf.beat_schedule = {
    'SAY-HELLO-EVERY-30-SECOND': {
        'task': 'tasks.hello',
        'schedule': 3.0,
        'args': ('name', )
   }
}

