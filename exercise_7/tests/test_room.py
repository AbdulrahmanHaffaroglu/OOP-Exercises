import pytest

from hotel_reservation_system.models import Room


class TestRoom:

    # -------------------------
    # Object creation
    # -------------------------

    def test_creation(self):
        room = Room(101, "single", 80)

        assert room.room_number == 101
        assert room.room_type == "single"
        assert room.price == 80
        assert room.available is True

    # -------------------------
    # Properties / getters
    # -------------------------

    def test_price_property_can_be_updated(self):
        room = Room(101, "single", 80)

        room.price = 100

        assert room.price == 100

    def test_repr_contains_room_information(self):
        room = Room(101, "single", 80)

        assert repr(room) == "Room(101, single, $80/night, available)"

    # -------------------------
    # Invalid inputs
    # -------------------------

    @pytest.mark.parametrize(
        "factory",
        [
            lambda: Room(0, "single", 80),
            lambda: Room(101, "penthouse", 80),
            lambda: Room(101, "single", -1),
            lambda: Room(101, "single", 80, "booked"),
        ],
    )
    def test_rejects_invalid_room_values(self, factory):
        with pytest.raises(ValueError):
            factory()

    def test_rejects_negative_price_update(self):
        room = Room(101, "single", 80)

        with pytest.raises(ValueError):
            room.price = -1

        assert room.price == 80
