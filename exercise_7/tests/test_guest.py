import pytest

from hotel_reservation_system.models import Guest


class TestGuest:

    # -------------------------
    # Object creation
    # -------------------------

    def test_creation(self):
        guest = Guest("G001", "Ada Lovelace", "ada@example.com")

        assert guest.guest_id == "G001"
        assert guest.name == "Ada Lovelace"
        assert guest.email == "ada@example.com"
        assert guest.reservations == []

    # -------------------------
    # Normal behavior
    # -------------------------

    def test_guest_tracks_reservations(self, hotel, rooms, guests, stay_dates):
        room = rooms[0]
        guest = guests[0]
        hotel.add_room(room)
        hotel.register_guest(guest)

        reservation = hotel.create_reservation(guest, room, *stay_dates)

        assert guest.reservations == [reservation]

    # -------------------------
    # Invalid inputs
    # -------------------------

    def test_duplicate_guest_ids_are_rejected(self, hotel, guests):
        hotel.register_guest(guests[0])
        duplicate = Guest("G001", "Different Guest", "different@example.com")

        with pytest.raises(ValueError):
            hotel.register_guest(duplicate)
