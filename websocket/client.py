import os
import socket
from pickle import dumps


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8585))
print('Connected')

with open('/home/mehdi/Desktop/kub_config', 'rb') as f:
    f.seek(0)
    while True:
        chunk = f.read(1024)
        if not chunk:
            break

        client.sendall(chunk)

client.close()
