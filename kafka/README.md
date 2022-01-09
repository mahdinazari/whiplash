### Run 
```
$ sudo docker-compose up
```

Now let's use the nc command to verify that both the servers are listening on the respective ports:
```
nc -z localhost 22181
Connection to localhost port 22181 [tcp/*] succeeded!

nc -z localhost 29092
Connection to localhost port 29092 [tcp/*] succeeded!
```

Or check the verbose logs while the containers are starting
```
sudo docker-compose logs kafka | grep -i started
```
Or check process
```
sudo docker-compose ps
```

#### Create topics
```
kafka-topics --bootstrap-server 127.0.0.1:9092 --create --partitions 3 --replication-factor 1 --topic first_topic
```

Dockerize
```
sudo docker exec -it mykafka kafka-topics --bootstrap-server 127.0.0.1:9092 --create --partitions 3 --replication-factor 1 --topic first_topic
```

#### List topics
```
kafka-topics --list --bootstrap-server 127.0.0.1:9092
```

Dockerize:
```
sudo docker exec -it mykafka kafka-topics --list --bootstrap-server localhost:29092
```

#### Topics info
```
kafka-topics --describe --bootstrap-server 127.0.0.1:9092 --topic first_topic
```

Dockerize:
```
sudo docker exec -it mykafka kafka-topics --describe --bootstrap-server localhost:29092 --topic first_topic
```

#### Create producer
```
kafka-console-producer --broker-list localhost:9092 --topic new-topic acks=1
```

Dockerize
```
sudo docker exec -it mykafka kafka-console-producer --broker-list localhost:9092 --topic new-topic acks=1
```

#### Create consumer
```
kafka-console-consumer --topic first_topic --from-beginning  --bootstrap-server localhost:9092
```

Dockerize
```
sudo docker exec -it mykafka kafka-console-consumer --topic first_topic --from-beginning  --bootstrap-server localhost:9092
```