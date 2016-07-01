class Emitter:
    channels = {}

    def subscribe(self, channel, callback):
        self.channels.setdefault(channel, [])
        self.channels[channel].append(callback)

    def unsubribe(self, channel, callbak):
        pass
        
    def emit(self, channel, data):
        channel = self.channels.get(channel, False)
        
        if channel:
            for callback in channel:
                callback(data)
