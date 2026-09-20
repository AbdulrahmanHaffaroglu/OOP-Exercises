import pytest

from hotel_reservation_system.models import Reservation


class TestReservation:

    # -------------------------
    # Object creation
    # -------------------------

    def test_creation(self, hotel, rooms, guests, stay_dates):
        room = rooms[0]
        guest = guests[0]
        hotel.add_room(room)
        hotel.register_guest(guest)

        reservation = hotel.create_reservation(guest, room, *stay_dates)

        assert reservation.guest is guest
        assert reservation.room is room
        assert reservation.status == "confirmed"
        assert reservation.calculate_nights() == 3
        assert reservation.calculate_price() == 240

    # -------------------------
    # Normal behavior
    # -------------------------

    def test_reservation_preserves_original_room_price(
        self, hotel, rooms, guests, stay_dates
    ):
        room = rooms[0]
        guest = guests[0]
        hotel.add_room(room)
        hotel.register_guest(guest)
        reservation = hotel.create_reservation(guest, room, *stay_dates)

        room.price = 150

        assert reservation.calculate_price() == 240

    def test_status_can_change_to_completed(self, hotel, rooms, guests, stay_dates):
        room = rooms[0]
        guest = guests[0]
        hotel.add_room(room)
        hotel.register_guest(guest)
        reservation = hotel.create_reservation(guest, room, *stay_dates)

        reservation.change_status("completed")

        assert reservation.status == "completed"

    # -------------------------
    # Invalid inputs
    # -------------------------

    @pytest.mark.parametrize(
        "status",
        ["unknown", "pending", "Completed"],
    )
    def test_rejects_unknown_status(
        self, status, hotel, rooms, guests, stay_dates
    ):
        room = rooms[0]
        guest = guests[0]
        hotel.add_room(room)
        hotel.register_guest(guest)
        reservation = hotel.create_reservation(guest, room, *stay_dates)

        with pytest.raises(ValueError):
            reservation.change_status(status)

        assert reservation.status == "confirmed"

    @pytest.mark.parametrize(
        "dates",
        [
            ("2026-10-04", "2026-10-01"),
            ("2026-10-01", "2026-10-01"),
        ],
    )
    def test_rejects_invalid_date_range(
        self, dates, hotel, rooms, guests
    ):
        from datetime import date

        room = rooms[0]
        guest = guests[0]
        hotel.add_room(room)
        hotel.register_guest(guest)
        check_in, check_out = (date.fromisoformat(value) for value in dates)

        with pytest.raises(ValueError):
            hotel.create_reservation(guest, room, check_in, check_out)

        assert hotel.reservations == []
        assert guest.reservations == []