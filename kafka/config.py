kafka_host = 'localhost'
kafka_port = '29092'
kafka_server1 = f'{kafka_host}:{kafka_port}'
topic_name = 'first_topic'
consumer_timeout = 100000
auto_offset_reset = 'earliest'
bootstrap_servers = [kafka_server1]