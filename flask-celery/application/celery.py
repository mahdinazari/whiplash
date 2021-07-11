from celery import Celery


celery = Celery('application')
celery.config_from_object('application.celery_config')


if __name__ == '__main__':
    celery.start()

