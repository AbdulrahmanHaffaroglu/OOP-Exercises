from .channel import Channel

class Email(Channel):
    def __init__(self, email):
        self.email = email

    def send(self, message, user=None):
        if user:
            print(f"{self.email} sent: {message}")
            print(f"this message was sent to {user}")

        else:
            print(f"{self.email} sent: {message}")