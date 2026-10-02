import pytest

from mini_uber_system.models.Rides.ride import Ride
from mini_uber_system.models.Rides.ride_item import RideItem


class TestRide:
	# Normal behavior and getters
	def test_register_and_find_ride_item(self, ride_setup):
		_, _, ride = ride_setup

		assert Ride.get_ride_item(ride.id) is ride
		assert RideItem.find_ride_item(ride.id) is ride

	def test_unknown_ride_id_is_rejected(self):
		with pytest.raises(ValueError, match='No ride found'):
			Ride.get_ride_item(999)