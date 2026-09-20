from .reservation import Reservation


class Hotel:
    def __init__(self):
        self.rooms = []
        self.guests = []
        self.reservations = []

    def add_room(self, room):
        if any(existing.room_number == room.room_number for existing in self.rooms):
            raise ValueError("a room with this number already exists")

        self.rooms.append(room)

    def register_guest(self, guest):
        if any(existing.guest_id == guest.guest_id for existing in self.guests):
            raise ValueError("a guest with this ID is already registered")

        self.guests.append(guest)

    def create_reservation(self, guest, room, check_in_date, check_out_date):
        if guest not in self.guests:
            raise ValueError("guest must be registered at the hotel")

        if room not in self.rooms:
            raise ValueError("room must belong to the hotel")

        if any(
            existing.room is room
            and existing.status == "confirmed"
            and check_in_date < existing.check_out_date
            and check_out_date > existing.check_in_date
            for existing in self.reservations
        ):
            raise ValueError("room is already reserved for those dates")

        reservation = Reservation(guest, room, check_in_date, check_out_date)
        self.add_reservation(reservation)
        return reservation

    def add_reservation(self, reservation):
        self.reservations.append(reservation)

    def complete_reservation(self, reservation):
        for r in self.reservations:
            if reservation == r:
                r.change_status("completed")
                r.room.available = True
                return

        raise ValueError("reservation does not belong to this hotel")

    def cancel_reservation(self, reservation):
        for r in self.reservations:
            if reservation == r:
                r.change_status("cancelled")
                r.room.available = True
                return

        raise ValueError("reservation does not belong to this hotel")

    def find_rooms_by_type(self, room_type):
        return [room for room in self.rooms if room.room_type == room_type]

    def find_room_available(self):
        return [room for room in self.rooms if room.available]