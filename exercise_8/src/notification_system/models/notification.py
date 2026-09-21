class Notification:
    def __init__(self, channel_types, message, user=None):

        self.channel_types = channel_types
        self.message = message
        self.user = user

    def send(self):
        for channel_type in self.channel_types:
            channel_type.send(self.message, self.user)

