import os
import json


class Config:
    WS_HOST = '0.0.0.0'
    WS_PORT = 9989

    # Redis
    REDIS_HOST = os.environ.get('REDIS_HOST', '127.0.0.1')
    REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
    REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', None)
    REDIS_DB = os.environ.get('REDIS_DB', 0)
