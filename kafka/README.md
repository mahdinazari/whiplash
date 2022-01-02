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
sudo docker exec -it mykafka kafka-topics --create --zookeeper myzookeeper:2181 --replication-factor 1 --partitions 1 --topic users
```

#### List topics
```
sudo docker exec -it mykafka kafka-topics --list --zookeeper myzookeeper:2181
```
