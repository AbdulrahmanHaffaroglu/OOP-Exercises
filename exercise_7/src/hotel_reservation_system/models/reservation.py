class Reservation:

    valid_status = ["confirmed", "cancelled", "completed"]

    def __init__(self, guest, room, check_in_date, check_out_date):
        if check_out_date <= check_in_date:
            raise ValueError("check-out date should be after check-in date")

        self.guest = guest
        self.room = room
        self._price = room.price
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self._status = "confirmed"
        room.available = False
        guest.reservations.append(self)

    def calculate_nights(self):
        return (self.check_out_date - self.check_in_date).days

    def calculate_price(self):
        return self._price * self.calculate_nights()

    def change_status(self, status):
        if status not in Reservation.valid_status:
            raise ValueError("this not a valid status for a reservation")

        if self._status == 'completed' and status == 'cancelled':
            raise ValueError("completed reservations can not be cancelled")

        if self._status == 'cancelled' and status == 'completed':
            raise ValueError("cancelled reservations can not be completed")

        self._status = status

    @property
    def status(self):
        return self._status

    def __repr__(self):
        return f"Reservation({self.guest.name}, room {self.room.room_number}, {self._status})"