from .channel import Channel

class SMS(Channel):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def send(self, message, user=None):
        if user:
            print(f"{self.phone_number} sent: {message}")
            print(f"this message was sent to {user}")
        else:
            print(f"{self.phone_number} sent: {message}")
