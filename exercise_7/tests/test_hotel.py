import pytest


class TestHotel:

    # -------------------------
    # Normal behavior
    # -------------------------

    def test_room_and_guest_registration(self, hotel, rooms, guests):
        for room in rooms:
            hotel.add_room(room)
        for guest in guests:
            hotel.register_guest(guest)

        assert hotel.rooms == list(rooms)
        assert hotel.guests == list(guests)

    def test_room_searches(self, hotel, rooms):
        for room in rooms:
            hotel.add_room(room)

        assert hotel.find_rooms_by_type("double") == [rooms[1]]
        assert hotel.find_room_available() == list(rooms)

    def test_cancelling_reservation_releases_room(
        self, hotel, rooms, guests, stay_dates
    ):
        room = rooms[0]
        hotel.add_room(room)
        hotel.register_guest(guests[0])
        reservation = hotel.create_reservation(guests[0], room, *stay_dates)

        assert room.available is False

        hotel.cancel_reservation(reservation)

        assert reservation.status == "cancelled"
        assert room.available is True

    def test_completing_reservation_releases_room(
        self, hotel, rooms, guests, stay_dates
    ):
        room = rooms[0]
        hotel.add_room(room)
        hotel.register_guest(guests[0])
        reservation = hotel.create_reservation(guests[0], room, *stay_dates)

        hotel.complete_reservation(reservation)

        assert reservation.status == "completed"
        assert room.available is True

    # -------------------------
    # Invalid inputs
    # -------------------------

    def test_overlapping_reservation_is_rejected_without_state_change(
        self, hotel, rooms, guests, stay_dates
    ):
        room = rooms[0]
        hotel.add_room(room)
        hotel.register_guest(guests[0])
        hotel.register_guest(guests[1])
        hotel.create_reservation(guests[0], room, *stay_dates)

        with pytest.raises(ValueError):
            hotel.create_reservation(
                guests[1], room, stay_dates[0], stay_dates[1]
            )

        assert len(hotel.reservations) == 1
        assert len(guests[1].reservations) == 0

    def test_unregistered_guest_is_rejected(self, hotel, rooms, guests, stay_dates):
        room = rooms[0]
        hotel.add_room(room)

        with pytest.raises(ValueError):
            hotel.create_reservation(guests[0], room, *stay_dates)

        assert hotel.reservations == []

    def test_duplicate_room_number_is_rejected(self, hotel):
        from hotel_reservation_system.models import Room

        hotel.add_room(Room(101, "single", 80))

        with pytest.raises(ValueError):
            hotel.add_room(Room(101, "double", 120))

        assert len(hotel.rooms) == 1

    def test_completed_reservation_cannot_be_cancelled(
        self, hotel, rooms, guests, stay_dates
    ):
        room = rooms[0]
        hotel.add_room(room)
        hotel.register_guest(guests[0])
        reservation = hotel.create_reservation(guests[0], room, *stay_dates)
        hotel.complete_reservation(reservation)

        with pytest.raises(ValueError):
            hotel.cancel_reservation(reservation)

        assert reservation.status == "completed"

    def test_cancelled_reservation_cannot_be_completed(
        self, hotel, rooms, guests, stay_dates
    ):
        room = rooms[0]
        hotel.add_room(room)
        hotel.register_guest(guests[0])
        reservation = hotel.create_reservation(guests[0], room, *stay_dates)
        hotel.cancel_reservation(reservation)

        with pytest.raises(ValueError):
            hotel.complete_reservation(reservation)

        assert reservation.status == "cancelled"