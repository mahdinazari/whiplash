import os


broker_url = os.environ.get(
    'CELERY_BROKER_URL',
    'redis://localhost:6379/0',
)

result_backend = os.environ.get(
    'CELERY_BACKEND_URL',
    'db+postgresql://postgres:postgres@localhost/practice'
)

include = ['tasks']
task_serializer = 'json'
result_serializer = 'json'
enable_utc = True
timezone = 'Asia/Tehran'
task_routes = {
    'tasks.add': {'queue': 'queue1'},
    'tasks.mul': {'queue': 'queue2'},
    'tasks.say_hello': {'queue': 'queue3'},
}

# limit number of requests at minute
# task_annotations = {'tasks.add': {'rate_limit': '40/m'}}
