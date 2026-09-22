import pytest

from vehicle_system.models.motorcycle import Motorcycle
from vehicle_system.models.register import Register


class TestMotorcycle:

    # -------------------------
    # Object creation
    # -------------------------

    def test_creation(self):
        motorcycle = Motorcycle("Honda", "CBR", 600)

        assert motorcycle.brand == "Honda"
        assert motorcycle.model == "CBR"
        assert motorcycle.engine_cc == 600
        assert motorcycle.status == "Stopped"
        assert motorcycle.fuel == 0

    # -------------------------
    # Normal behavior
    # -------------------------

    def test_start_and_stop(self):
        motorcycle = Motorcycle("Honda", "CBR", 600)
        Register.add(motorcycle)
        motorcycle.refuel(20)

        motorcycle.start_vehicle()
        assert motorcycle.status == "Running"
        assert motorcycle.engine.status == "Running"

        motorcycle.stop_vehicle()
        assert motorcycle.status == "Stopped"
        assert motorcycle.engine.status == "Stopped"

    def test_trip_consumes_three_percent(self):
        motorcycle = Motorcycle("Honda", "CBR", 600)
        Register.add(motorcycle)
        motorcycle.refuel(20)
        motorcycle.start_vehicle()

        motorcycle.start_trip()
        motorcycle.finish_trip()

        assert motorcycle.fuel == 17
        assert motorcycle.status == "Running"

    # -------------------------
    # Properties / details
    # -------------------------

    def test_show_details(self, capsys):
        motorcycle = Motorcycle("Honda", "CBR", 600)
        motorcycle.show_details()
        details = capsys.readouterr().out

        assert "Type: Motorcycle" in details
        assert "Brand: Honda" in details
        assert "Engine capacity: 600cc" in details

    # -------------------------
    # Invalid inputs and edge cases
    # -------------------------

    def test_cannot_start_without_enough_fuel(self):
        motorcycle = Motorcycle("Honda", "CBR", 600)
        Register.add(motorcycle)

        with pytest.raises(ValueError):
            motorcycle.start_vehicle()

    def test_cannot_finish_a_trip_that_has_not_started(self):
        motorcycle = Motorcycle("Honda", "CBR", 600)

        with pytest.raises(ValueError):
            motorcycle.finish_trip()
