import json

from redis_client import r
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

        self.ws_server.set_fn_message_received(self._ws_recv_message)
        self.ws_server.run_forever()

    def _ws_new_client(self, client, server):
        import pudb; pudb.set_trace()
        self.ws_clients.append(client)

    def new_client(self, client, server): 
        server.send_message_to_all("Hey all, a new client has joined us")

    def _ws_recv_message(self, client, server, message):
        import pudb; pudb.set_trace()
        msg = json.loads(message)
        if msg['type'] == 'send':
            client['id'] = msg['sender_id']
            if client['id'] not in [f['id'] for f in self.ws_clients]:
                self.ws_server.set_fn_new_client(self._ws_new_client)
            
        elif msg['type'] == 'seen':
            client['id'] = msg['receiver_id']
            if client['id'] not in [f['id'] for f in self.ws_clients]:
                self.ws_server.set_fn_new_client(self._ws_new_client)
                
        user = r.hgetall("user")
        # destination_client = [f for f in self.ws_clients if f['id'] == msg['receiver_id']]
        # if not destination_client:
        #     self.new_client(destination_client, server)
        #     self.ws_server.set_fn_new_client(self.new_client)
        
        print(20 * '*')
        print(self.ws_clients)
        print(20 * '*')
        self.dispature.consume(msg, client, server)
        # self._ws_close_client(client)

    def _ws_close_client(self, client):
        import pudb; pudb.set_trace()
        self.ws_clients.remove(client)

    def ws_send_message(self, msg):
        import pudb; pudb.set_trace()
        message = json.dumps(msg)
        if self.ws_server:
            try:
                self.ws_server.send_message_to_all(message)

            except Exception as e:
                print("ws_send_message", str(e))


if __name__ == '__main__':
    web_socket = WebSocketManager(Config.WS_HOST, Config.WS_PORT)
    web_socket.start_websocket()
