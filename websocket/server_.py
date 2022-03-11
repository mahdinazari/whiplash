import os
import time
import socket
from pickle import loads
from threading import Thread

import tqdm


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8585))
server.listen()


def client_handler(connection, address):
    print(f'New Client "{address}" Has Been Connected')
    file_size = os.path.getsize('/home/mehdi/Desktop/kub_config')
    progress = tqdm.tqdm(range(file_size), f"Receiving main.txt", unit="B", unit_scale=True, unit_divisor=1024)
    with open('main.txt', 'wb') as f:
        while True:
            data = connection.recv(1024)
            if not data:
                break

            f.write(data)
            progress.update(len(data))
            time.sleep(1)

    connection.close()
    print('File Has Been Saved')


while True:
    print('server is listening')
    connection, address = server.accept()
    import pudb; pudb.set_trace()
    t = Thread(
        target=client_handler,
        kwargs={'connection': connection, 'address': address}
    )
    t.start()
