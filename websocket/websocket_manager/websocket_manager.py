import json

from config import Config
from dispature import Dispature
from message_handler import MessageHandler
from websocket_server import WebsocketServer


class WebSocketManager:
    def __init__(self, host, port):
        self.ws_port = port
        self.ws_host = host
        self.ws_server = None
        self.ws_clients = []
        self.dispature = Dispature(
            [
                MessageHandler(),
            ]
        )

    def start_websocket(self):
        print('Websocket Has Been Started ...')
        self.ws_server = WebsocketServer(self.ws_port, host=self.ws_host)
        self.ws_server.set_fn_new_client(self._ws_new_client)
        self.ws_server.set_fn_message_received(self._ws_recv_message)
        self.ws_server.run_forever()

    def _ws_new_client(self, client, server):
        self.ws_clients.append(client)

    def _ws_recv_message(self, client, server, message):
        msg = json.loads(message)
        self.dispature.consume(msg)

    def _ws_close_client(self, client, server):
        self.ws_clients.remove(client)

    def ws_send_message(self, msg):
        message = json.dumps(msg)
        if self.ws_server:
            try:
                self.ws_server.send_message_to_all(message)

            except Exception as e:
                print("ws_send_message", str(e))


if __name__ == '__main__':
    web_socket = WebSocketManager(Config.HOST, Config.PORT)
    web_socket.start_websocket()
