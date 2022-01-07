import json

from kafka import KafkaProducer, KafkaConsumer

import config


def get_producer():
    pass

def publish_message():
    pass

def subscribe_message():
    pass


if __name__ == '__main__':
    producer = KafkaProducer(
    bootstrap_servers=config.bootstrap_servers,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    metrics = producer.metrics()
    print(metrics)
    producer.send(config.topic_name, {'topic': 'linuxhint'})

    consumer = KafkaConsumer(
        config.topic_name, 
        auto_offset_reset=config.auto_offset_reset,
        bootstrap_servers=config.bootstrap_servers, 
        consumer_timeout_ms=config.consumer_timeout,
    )
    print('Assigning Topic.')
    for message in consumer:
        print('--------------------------------------------------------------')
        print(message.value)
        print("OFFSET: " + str(message[0])+ "\t MSG: " + str(message))
        