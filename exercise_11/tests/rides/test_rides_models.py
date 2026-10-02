import pytest

from mini_uber_system.models.Rides.ride_item import RideItem
from mini_uber_system.models.Users.passenger import Passenger


class TestRideItem:
	# Object creation
	def test_creation_calculates_fare_and_initial_state(self, ride_setup):
		_, passenger, ride = ride_setup

		assert ride.pickup_location == 'Istanbul'
		assert ride.destination == 'Bursa'
		assert ride.num_of_passengers == 2
		assert ride.vehicle_type == 'standart_car'
		assert ride.passenger is passenger
		assert ride.base_fare == 50
		assert ride.price_per_kilometer == 15
		assert ride.total_price == 200
		assert ride.unpaid_price == 200
		assert ride.status == 'Requested'
		assert ride.is_payed is False

	# Normal behavior
	def test_ride_lifecycle(self, ride_setup):
		_, _, ride = ride_setup

		ride.accept_ride()
		assert ride.status == 'Accepted'
		ride.start_ride()
		assert ride.status == 'In_Progress'
		ride.complete_ride()
		assert ride.status == 'Completed'

	def test_display_shows_ride_details(self, ride_setup, capsys):
		_, _, ride = ride_setup

		ride.display()

		output = capsys.readouterr().out
		assert 'Passenger: Passenger One' in output
		assert 'Pickup: Istanbul' in output
		assert 'Destination: Bursa' in output
		assert 'Total price: 200' in output

	# Invalid inputs and state transitions
	def test_vehicle_capacity_is_enforced(self, ride_setup):
		_, passenger, _ = ride_setup

		with pytest.raises(ValueError, match='amount of passengers'):
			RideItem('Istanbul', 'Bursa', 5, 'standart_car', 10, passenger)

	def test_ride_requires_an_available_driver(self):
		passenger = Passenger('Passenger One', 9876543210)

		with pytest.raises(ValueError, match='no available rider'):
			RideItem('Istanbul', 'Bursa', 1, 'motorcycle', 10, passenger)

	def test_lifecycle_methods_reject_invalid_state(self, ride_setup):
		_, _, ride = ride_setup

		with pytest.raises(ValueError, match='status.*Accepted'):
			ride.start_ride()
		with pytest.raises(ValueError, match='status.*In_Progress'):
			ride.complete_ride()

	# Edge cases
	def test_requested_ride_can_be_cancelled(self, ride_setup):
		_, _, ride = ride_setup

		ride.cancell_ride()

		assert ride.status == 'Cancelled'
