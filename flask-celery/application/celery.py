from celery import Celery


celery = Celery('tasks')
celery.config_from_object('application.celeryconfig')


if __name__ == '__main__':
    celery.start()

