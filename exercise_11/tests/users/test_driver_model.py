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
def driver_and_ride():
	vehicle = Vehicle.create_vehicle('standart_car')
	driver = Driver('Driver One', 1234567890, vehicle)
	passenger = Passenger('Passenger One', 9876543210)
	ride = RideItem('Istanbul', 'Bursa', 2, 'standart_car', 10, passenger)
	return driver, ride


class TestDriver:
	# Object creation and registration
	def test_creation_registers_driver(self):
		vehicle = Vehicle.create_vehicle('standart_car')

		driver = Driver('Driver One', 1234567890, vehicle)

		assert driver.id == 'driver-001'
		assert driver.status == 'Available'
		assert driver.vehicle_id == vehicle.id
		assert driver.vehicle_type == 'standart_car'
		assert DriverRegistry.drivers[driver.id] is driver

	# Normal behavior
	def test_registry_finds_only_available_matching_driver(self):
		vehicle = Vehicle.create_vehicle('standart_car')
		driver = Driver('Driver One', 1234567890, vehicle)

		assert Driver.find_available_driver('standart_car') is driver
		assert DriverRegistry.find_available('motorcycle') is None
		driver.change_status('Busy')
		assert Driver.find_available_driver('standart_car') is None

	def test_register_vehicle(self):
		driver = Driver('Driver One', 1234567890)
		vehicle = Vehicle.create_vehicle('motorcycle')

		driver.register_vehicle(vehicle)

		assert driver.vehicle_id == vehicle.id
		assert driver.vehicle_type == 'motorcycle'

	def test_accept_start_and_complete_ride(self, driver_and_ride, capsys):
		driver, ride = driver_and_ride

		driver.accept_ride(ride)
		assert driver.status == 'Busy'
		assert driver.current_ride_id == ride.id
		assert driver.ride_history == [ride.id]
		assert ride.status == 'Accepted'

		driver.start_ride()
		assert ride.status == 'In_Progress'

		driver.complete_ride()
		assert ride.status == 'Completed'
		assert driver.current_ride_id is None
		assert driver.status == 'Active'
		assert 'total price for ride' in capsys.readouterr().out

	# Invalid inputs and state transitions
	def test_invalid_phone_number(self):
		with pytest.raises(ValueError):
			Driver('Driver One', 123)

	def test_cannot_register_second_vehicle(self):
		first_vehicle = Vehicle.create_vehicle('standart_car')
		second_vehicle = Vehicle.create_vehicle('motorcycle')
		driver = Driver('Driver One', 1234567890, first_vehicle)

		with pytest.raises(ValueError, match='already registered'):
			driver.register_vehicle(second_vehicle)

	def test_cannot_accept_ride_without_vehicle(self):
		vehicle = Vehicle.create_vehicle('standart_car')
		Driver('Registered Driver', 1234567890, vehicle)
		driver_without_vehicle = Driver('Driver Two', 1111111111)
		ride = RideItem(
			'Istanbul', 'Bursa', 1, 'standart_car', 10,
			Passenger('Passenger One', 9876543210),
		)

		with pytest.raises(ValueError, match='register a vehicle'):
			driver_without_vehicle.accept_ride(ride)

	def test_cannot_accept_different_vehicle_type(self, driver_and_ride):
		driver, ride = driver_and_ride
		motorcycle_driver = Driver(
			'Driver Two', 1111111111, Vehicle.create_vehicle('motorcycle')
		)

		with pytest.raises(ValueError, match='this ride request'):
			motorcycle_driver.accept_ride(ride)

	def test_cannot_change_to_current_status(self):
		driver = Driver('Driver One', 1234567890)

		with pytest.raises(ValueError, match='already Available'):
			driver.change_status('Available')
