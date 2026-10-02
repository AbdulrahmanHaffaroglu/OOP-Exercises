import pytest

from mini_uber_system.models.Rides.ride import Ride
from mini_uber_system.models.Rides.ride_item import RideItem
from mini_uber_system.models.Users.driver import Driver
from mini_uber_system.models.Users.driver_registry import DriverRegistry
from mini_uber_system.models.Users.passenger import Passenger
from mini_uber_system.models.Vehicles.vehicle import Vehicle


@pytest.fixture(autouse=True)
def reset_model_registries():
	Ride._ride_items.clear()
	Ride.id = 1
	Vehicle._vehicle_items.clear()
	Vehicle.id = 1
	DriverRegistry.drivers.clear()
	DriverRegistry.id_num = 1


@pytest.fixture
def ride_setup():
	vehicle = Vehicle.create_vehicle('standart_car')
	driver = Driver('Driver One', 1234567890, vehicle)
	passenger = Passenger('Passenger One', 9876543210)
	ride = RideItem('Istanbul', 'Bursa', 2, 'standart_car', 10, passenger)
	return driver, passenger, ride