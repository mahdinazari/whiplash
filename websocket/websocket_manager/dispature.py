class Dispature:
    def __init__(self, handlers):
        self.handlers = handlers
        self.message = None

    def consume(self, message, client, server):
        import pudb; pudb.set_trace()
        try:
            self.message = message
            if self.message and len(self.handlers) > 0:
                for handler in self.handlers:
                    if 'message' in self.message or 'sender_id' in self.message or 'receiver_id' in self.message \
                            or 'direct' not in self.message:
                        handler.apply_handler(self.message, client, server)

        except Exception as e:
            print(e)


    # try:
    #     ws = websocket.WebSocket()
    #     ws.connect("ws://{}:{}/".format(
    #         config['ip_port']['printer_ip'],
    #         config['ip_port']['printer_port']
    #     ))
    #     ws.send(json.dumps(
    #         {
    #             'cmd': 'upload_print',
    #             'password': manager.kiosk_fsm.zip_random_password,
    #             'directory': 'ftp://{}/{}'.format(
    #                 config['ftp_config']['ftp_ip'],
    #                 directory,
    #             )
    #         }
    #     ))
    #     ws.close()
    #     return True, None
