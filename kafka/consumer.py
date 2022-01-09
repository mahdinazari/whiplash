import json

from kafka import KafkaConsumer

import config


def is_json(input):
  try:
    json.loads(input)

  except ValueError as e:
    return False

  return True


def get_consumer():
    consumer = None
    try:
        consumer = KafkaConsumer(
            config.topic_name, 
            auto_offset_reset=config.auto_offset_reset,
            bootstrap_servers=config.bootstrap_servers, 
            consumer_timeout_ms=config.consumer_timeout,
        )

    except Exception as e:
        pass
    
    finally:
        return consumer
        

def subscribe_message(consumer):
    print('Assigning Topic.')
    for message in consumer:
        print('-' * 50)
        if not is_json(message.value):
            message = {'message': message.value}
            print(message)

        else:    
            data = json.loads((message.value).decode())
            json.dumps(data)
            print(message.value)
        

if __name__ == '__main__':
    consumer = get_consumer()
    if not consumer:
        print('Get Consumer Exception!')
    
    subscribe_message(consumer)
