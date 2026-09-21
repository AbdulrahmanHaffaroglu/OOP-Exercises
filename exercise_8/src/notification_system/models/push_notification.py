from .channel import Channel

class PushNotification(Channel):
    def __init__(self, device_id):
        self.device_id = device_id

    def send(self, message, user=None):
        print(f"send to {self.device_id}: {message}")