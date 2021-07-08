# flask-docker
`Dockerize` a minimal `Flask` application with `redis`.

#### Application requirements
```
flask
redis
```

#### Docker requirements
```
sudo doker pull python:3.6
sudo docker pull redis
```

#### Dockerfile
```
FROM python:3.6                                                                
WORKDIR /code                                                                  
COPY . .                                                                       
RUN pip install -r requirements.txt                                            
ENV FLASK_APP=app.py                                                           
ENV FLASK_RUN_HOST=0.0.0.0                                                     
CMD ["flask", "run"]   
```

#### Create network
```
sudo docker network create myapp_network
```

#### Run redis 
```
sudo docker run --it --name redis --rm -v /tmp/data:/data --network myapp_network redis
```

#### Insert to redis
```
sudo docker exec -it redis "redis-cli"

set name <NAME>
```

#### Build myapp
```
sudo docker build -t myapp:v1 .
```

#### Run myapp
```
sudo docker run -it --name myapp --rm -p 5000:5000 --network myapp_network myapp:v1
```

#### Request the hello API
```
curl localhost:5000/hello
```

#### Output
```
hello mehdi
```

Other way to run application is using the `docker-compose`.
## Run application using docker-compose

#### Make docker-compose.yml
```
version: "3.9"                                                                                                           
services:                                                                                                                
  web:                                                                                                                   
    build: .                                                                                                             
    image: "myapp:v1"                                                                                                    
    container_name: "myapp"                                                                                              
    ports:                                                                                                               
      - "5000:5000"                                                                                                      
                                                                                                                         
  redis:                                                                                                                 
    image: "redis:latest"                                                                                                
    container_name: "redis"                                                                                              
    volumes:               
```

#### Run docker-compose
```
sudo docker-compose -d up
```

#### Request the hello API
```
curl localhost:5000/hello
```

#### Output
```
hello mehdi
```
