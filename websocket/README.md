#### Install node, npm and wscat
```
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash
nvm --version
nvm install node

npm install -g wscat
```

#### Call websocket
```
ws://localhost:9989/  w 1 -x '{"action": "helloWorld"}'
```