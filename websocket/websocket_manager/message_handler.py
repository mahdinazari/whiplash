from redis_client import lpush, get_message_by_id, lpop


class MessageHandler:
    def apply_handler(self, message, client, server):
        import pudb; pudb.set_trace()
        if message['type'] == 'seen':
            queue = message['direct']
            messages = get_message_by_id(queue)
            for message in messages:
                print(messages)
                server.send_message(client, message)
                lpop(queue)
        
        elif message['type'] == 'send':
            queue = message['direct']
            lpush(queue, message)
            messages = get_message_by_id(queue)
            print(messages)
            # for message in messages:
            #     print(messages)
            #     server.send_message(client, message)
            #     lpop(queue)
            