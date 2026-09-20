class Guest:
    def __init__(self, guest_id, name, email):
        self.guest_id = guest_id
        self.name = name
        self.email = email

        self.reservations = []

    def __repr__(self):
        return f"Guest({self.guest_id}, {self.name})"
