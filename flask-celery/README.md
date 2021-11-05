# flask-celery
Implement `flask` application with `celery`.

### Run celery
```
./celery
```

or 
```
celery -A application worker -Q celery,queue1,queue2,queue3 --loglevel=INFO
```

### Run flask
```
python3 ./develop.py
```

### Call applicaion
```
curl localhost:5000/api/v1/index/
```
