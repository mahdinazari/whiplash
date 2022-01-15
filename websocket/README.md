#### Install node, npm and wscat
```
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash
nvm --version
nvm install node

npm install -g wscat
```

#### Call websocket
```
wscat -c ws://localhost:9989/  w 1 -x '{"sender": "client1", sender_id": 1, "type": "seen", "message": "helloWorld", "receiver_id": 2, "direct": 1}'
```