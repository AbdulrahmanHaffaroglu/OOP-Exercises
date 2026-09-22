import pytest

from vehicle_system.models.car import Car
from vehicle_system.models.register import Register


class TestRegister:

    def setup_method(self):
        Register.registered_vehicles.clear()

    # -------------------------
    # Normal behavior
    # -------------------------

    def test_add_assigns_unique_id(self):
        first_car = Car("Toyota", "Corolla", 5)
        second_car = Car("Honda", "Civic", 5)

        Register.add(first_car)
        Register.add(second_car)

        assert first_car.id is not None
        assert second_car.id is not None
        assert first_car.id != second_car.id
        assert Register.registered_vehicles == [first_car, second_car]

    def test_remove_clears_vehicle_id(self):
        car = Car("Toyota", "Corolla", 5)
        Register.add(car)

        Register.remove(car)

        assert car.id is None
        assert car not in Register.registered_vehicles

    # -------------------------
    # Invalid inputs
    # -------------------------

    def test_cannot_add_same_vehicle_twice(self):
        car = Car("Toyota", "Corolla", 5)
        Register.add(car)

        with pytest.raises(ValueError):
            Register.add(car)

    def test_cannot_remove_unregistered_vehicle(self):
        car = Car("Toyota", "Corolla", 5)

        with pytest.raises(ValueError):
            Register.remove(car)
