import json
import pprint

from kafka import KafkaProducer, KafkaConsumer, TopicPartition


producer = KafkaProducer(
    bootstrap_servers='localhost:29092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)


consumer = KafkaConsumer(bootstrap_servers='localhost:29092')


if __name__ == '__main__':
    metrics = producer.metrics()
    producer.send('linuxhint', {'topic': 'linuxhint'})


    print('Assigning Topic.')
    consumer.assign([TopicPartition('linuxhint', 2)])
    for message in consumer:
        print("OFFSET: " + str(message[0])+ "\t MSG: " + str(message))
        