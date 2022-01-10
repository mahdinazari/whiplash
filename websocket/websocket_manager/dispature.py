class Dispature:
    def __init__(self, handlers):
        self.handlers = handlers
        self.message = None

    def consume(self, message):
        try:
            self.message = message
            if self.message and len(self.handlers) > 0:
                for handler in self.handlers:
                    if 'message' in self.message or 'sender_id' in self.message or 'receiver_id' in self.message \
                            or 'direct' not in self.message:
                        handler.apply_handler(self.message)

        except Exception as e:
            print(e)
