import json
import time

from kafka import KafkaProducer

import config


def get_fake_messages(file_path=None):
    if not file_path:
        file_path = './fake_message.json'
    
    with open(file_path, 'r') as f:
        messages = json.load(f)
        return messages


def get_producer():
    producer = None
    try:
        producer = KafkaProducer(
            bootstrap_servers=config.bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
    
    except Exception as e:
        pass
    
    finally:
        return producer


def get_metric(producer):
    if not producer:
        print("Get Producer Exception!")
        return

    metrics = producer.metrics()
    print(metrics)


def publish_message(producer, topic_name, message):
    try:
        for message in messages:
            producer.send(topic_name, message)
    
        time.sleep(0.1)

    except Exception as e:
        pass


if __name__ == '__main__':
    print('Producer Is Running...')
    producer = get_producer()
    if not producer:
        print('Get Producer Exception!')

    messages = get_fake_messages()
    publish_message(producer, config.topic_name, messages)

    # message = {'topic': 'linuxhint'}
    # print(message)
    
