import pytest

from vehicle_system.models.register import Register
from vehicle_system.models.truck import Truck


class TestTruck:

    # -------------------------
    # Object creation
    # -------------------------

    def test_creation(self):
        truck = Truck("FH", "Volvo", 20)

        assert truck.model == "FH"
        assert truck.brand == "Volvo"
        assert truck.cargo_storage == 20
        assert truck.status == "Stopped"
        assert truck.fuel == 0

    # -------------------------
    # Normal behavior
    # -------------------------

    def test_start_and_stop(self):
        truck = Truck("FH", "Volvo", 20)
        Register.add(truck)
        truck.refuel(20)

        truck.start_vehicle()
        assert truck.status == "Running"
        assert truck.engine.status == "Running"

        truck.stop_vehicle()
        assert truck.status == "Stopped"
        assert truck.engine.status == "Stopped"

    def test_trip_consumes_ten_percent(self):
        truck = Truck("FH", "Volvo", 20)
        Register.add(truck)
        truck.refuel(20)
        truck.start_vehicle()

        truck.start_trip()
        truck.finish_trip()

        assert truck.fuel == 10
        assert truck.status == "Running"

    # -------------------------
    # Properties / details
    # -------------------------

    def test_show_details(self, capsys):
        truck = Truck("FH", "Volvo", 20)
        truck.show_details()
        details = capsys.readouterr().out

        assert "Type: Truck" in details
        assert "Brand: Volvo" in details
        assert "Cargo storage: 20" in details

    # -------------------------
    # Invalid inputs and edge cases
    # -------------------------

    def test_cannot_start_trip_without_enough_fuel(self):
        truck = Truck("FH", "Volvo", 20)
        Register.add(truck)
        truck.refuel(9)
        truck.start_vehicle()

        with pytest.raises(ValueError):
            truck.start_trip()

    def test_cannot_start_two_trips(self):
        truck = Truck("FH", "Volvo", 20)
        Register.add(truck)
        truck.refuel(20)
        truck.start_vehicle()
        truck.start_trip()

        with pytest.raises(ValueError):
            truck.start_trip()
