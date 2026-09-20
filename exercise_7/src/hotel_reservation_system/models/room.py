class Room:
    valid_types = {"single", "double", "suite"}

    def __init__(self, room_number, room_type, price, status="available"):
        if room_number <= 0:
            raise ValueError("room number must be positive")

        if room_type not in Room.valid_types:
            raise ValueError("invalid room type")

        if price < 0:
            raise ValueError("room price cannot be negative")

        if status not in {"available", "unavailable"}:
            raise ValueError("invalid room status")


        self.room_number = room_number
        self.room_type = room_type
        self._price = price
        self.available = status == "available"

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("room price cannot be negative")

        self._price = value

    def __repr__(self):
        availability = "available" if self.available else "unavailable"
        return f"Room({self.room_number}, {self.room_type}, ${self.price}/night, {availability})"