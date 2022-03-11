import json
import redis

from config import Config


r = redis.Redis(
    host=Config.REDIS_HOST,
    port=Config.REDIS_PORT, 
    db=Config.REDIS_DB
    #password=Config.REDIS_PASSWORD,
)


def lpush(queue, message):
    try:
        r.lpush(queue, json.dumps(message))

    except Exception as e:
        print(f'Push Exception - {e}')


def get_message_by_id(member_id, start=0, end=-1):
    messages = r.lrange(member_id, start, end)
    return messages


def lpop(queue):
    try:
        r.lpop(queue)
        
    except Exception as e:
        print('Pop Exception - %e')
        