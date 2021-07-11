import os


broker_url = os.environ.get(
    'CELERY_BROKER_URL',
    'redis://localhost:6379/0'
)
result_backend = os.environ.get(
    'CELERY_BACKEND_URL',
    'db+postgresql://postgres:postgres@localhost/practice'
)
include = ['application.tasks']
task_serializer = 'json'
result_serializer = 'json'
timezone = 'asia/tehran'
enable_utc = True
task_routes = {
    'application.tasks.add': {'queue': 'queue1'},
    'application.tasks.mul': {'queue': 'queue2'},
}

