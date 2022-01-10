from redis_client import lpush, get_message_by_id


class MessageHandler:
    def apply_handler(self, message):
        queue = message['sender']
        lpush(queue, message)
        messages = get_message_by_id(queue)
        for message in messages:
            print(message)
