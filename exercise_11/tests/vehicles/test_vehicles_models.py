import pytest
from mini_uber_system.models.Vehicles.motorcycle import Motorcycle
from mini_uber_system.models.Vehicles.premium_car import PremiumCar
from mini_uber_system.models.Vehicles.standart_car import StandartCar
from mini_uber_system.models.Vehicles.vehicle import Vehicle


@pytest.fixture(autouse=True)
def reset_vehicle_registry():
    Vehicle._vehicle_items.clear()
    Vehicle.id = 1


class TestVehicle:
    # Object creation

    def test_creation(self):
        standard = Vehicle.create_vehicle('standart_car')
        premium = Vehicle.create_vehicle('premium_car')
        motorcycle = Vehicle.create_vehicle('motorcycle')

        assert isinstance(standard, StandartCar)
        assert isinstance(premium, PremiumCar)
        assert isinstance(motorcycle, Motorcycle)
        assert standard.max_passengers == 4
        assert premium.max_passengers == 4
        assert motorcycle.max_passengers == 1


    # Normal behavior and getters
    def test_get_vehicle_prices_method(self):
        assert Vehicle.get_vehicle_prices('standart_car') == {
            'base_fare': 50, 'price_per_kilometer': 15
        }
        assert Vehicle.get_vehicle_prices('premium_car') == {
            'base_fare': 100, 'price_per_kilometer': 25
        }
        assert Vehicle.get_vehicle_prices('motorcycle') == {
            'base_fare': 30, 'price_per_kilometer': 10
        }


    def test_get_max_passengers_method(self):
        assert Vehicle.get_max_passengers('standart_car') == 4
        assert Vehicle.get_max_passengers('premium_car') == 4
        assert Vehicle.get_max_passengers('motorcycle') == 1


    def test_get_vehicle_method(self):
        vehicle = Vehicle.create_vehicle('standart_car')

        assert Vehicle.get_vehicle(vehicle.id) is vehicle


    def test_vehicle_ids_are_unique(self):
        first = Vehicle.create_vehicle('standart_car')
        second = Vehicle.create_vehicle('motorcycle')

        assert first.id != second.id


    # Invalid inputs

    def test_invalid_vehicle_type(self):
        with pytest.raises(ValueError):
            Vehicle.create_vehicle('bus')

    def test_invalid_vehicle_queries(self):
        with pytest.raises(ValueError):
            Vehicle.get_vehicle_prices('bus')
        with pytest.raises(ValueError):
            Vehicle.get_max_passengers('bus')
        with pytest.raises(ValueError):
            Vehicle.get_vehicle(999)

    @pytest.mark.parametrize(
        'max_passengers,base_fare,price_per_kilometer',
        [(0, 50, 10), (1, -1, 10), (1, 0, 0)],
    )
    def test_invalid_vehicle_configuration(
        self, max_passengers, base_fare, price_per_kilometer
    ):
        with pytest.raises(ValueError):
            StandartCar(
                max_passengers, base_fare, price_per_kilometer, 'standart_car'
            )