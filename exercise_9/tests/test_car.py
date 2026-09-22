import pytest

from vehicle_system.models.car import Car
from vehicle_system.models.register import Register


class TestCar:

    # -------------------------
    # Object creation
    # -------------------------

    def test_creation(self):
        car = Car("Toyota", "Corolla", 5)

        assert car.brand == "Toyota"
        assert car.model == "Corolla"
        assert car.max_passengers == 5
        assert car.status == "Stopped"
        assert car.fuel == 0

    # -------------------------
    # Normal behavior
    # -------------------------

    def test_start_and_stop(self):
        car = Car("Toyota", "Corolla", 5)
        Register.add(car)
        car.refuel(20)

        car.start_vehicle()
        assert car.status == "Running"
        assert car.engine.status == "Running"

        car.stop_vehicle()
        assert car.status == "Stopped"
        assert car.engine.status == "Stopped"

    def test_trip_consumes_five_percent(self):
        car = Car("Toyota", "Corolla", 5)
        Register.add(car)
        car.refuel(20)
        car.start_vehicle()

        car.start_trip()
        assert car.status == "On trip"
        car.finish_trip()

        assert car.fuel == 15
        assert car.status == "Running"
        assert car.on_trip is False

    def test_refuel_returns_new_fuel_level(self):
        car = Car("Toyota", "Corolla", 5)

        result = car.refuel(35)

        assert result == 35
        assert car.fuel == 35

    # -------------------------
    # Properties / details
    # -------------------------

    def test_show_details(self, capsys):
        car = Car("Toyota", "Corolla", 5)
        Register.add(car)
        car.refuel(35)

        car.show_details()
        details = capsys.readouterr().out

        assert "Type: Car" in details
        assert "Brand: Toyota" in details
        assert "Fuel: 35%" in details
        assert "Max passengers: 5" in details

    # -------------------------
    # Invalid inputs and edge cases
    # -------------------------

    def test_cannot_start_before_registration(self):
        car = Car("Toyota", "Corolla", 5)
        car.refuel(20)

        with pytest.raises(ValueError):
            car.start_vehicle()

    def test_cannot_start_trip_while_stopped(self):
        car = Car("Toyota", "Corolla", 5)
        Register.add(car)

        with pytest.raises(ValueError):
            car.start_trip()

    def test_cannot_stop_during_trip(self):
        car = Car("Toyota", "Corolla", 5)
        Register.add(car)
        car.refuel(20)
        car.start_vehicle()
        car.start_trip()

        with pytest.raises(ValueError):
            car.stop_vehicle()

    def test_cannot_refuel_running_car(self):
        car = Car("Toyota", "Corolla", 5)
        Register.add(car)
        car.refuel(20)
        car.start_vehicle()

        with pytest.raises(ValueError):
            car.refuel(10)

    def test_cannot_refuel_above_full(self):
        car = Car("Toyota", "Corolla", 5)

        with pytest.raises(ValueError):
            car.refuel(101)
