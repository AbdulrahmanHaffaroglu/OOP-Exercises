import pytest

from mini_uber_system.models.Payment_Methods.cash import Cash
from mini_uber_system.models.Payment_Methods.payment import Payment
from mini_uber_system.models.Rides.ride import Ride
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
    Passenger.id_num = 1


@pytest.fixture
def passenger_with_ride():
    Vehicle.create_vehicle('standart_car')
    Driver('Driver One', 1234567890, Vehicle.get_vehicle(1))
    passenger = Passenger('Passenger One', 9876543210, cash_method=Cash())
    ride = passenger.make_ride_request('Istanbul', 'Bursa', 2, 'standart_car', 10)
    return passenger, ride


def complete_ride(ride):
    ride.accept_ride()
    ride.start_ride()
    ride.complete_ride()


class TestPassenger:
    # Object creation
    def test_creation(self):
        passenger = Passenger('Passenger One', 9876543210)

        assert passenger.name == 'Passenger One'
        assert passenger.phone_number == 9876543210
        assert passenger.current_ride_id is None
        assert passenger.ride_history == []
        assert passenger.is_payed is False

    # Normal behavior
    def test_make_ride_request_updates_passenger_history(self, passenger_with_ride):
        passenger, ride = passenger_with_ride

        assert passenger.current_ride_id == ride.id
        assert passenger.ride_history == [ride.id]
        assert ride.passenger is passenger
        assert ride.total_price == 200

    def test_cannot_request_another_active_ride(self, passenger_with_ride):
        passenger, _ = passenger_with_ride

        with pytest.raises(ValueError, match='more than one ride'):
            passenger.make_ride_request('Bursa', 'Ankara', 1, 'standart_car', 5)

    def test_partial_payment_keeps_ride_active(self, passenger_with_ride):
        passenger, ride = passenger_with_ride
        complete_ride(ride)

        passenger.pay_ride(75, passenger.payment_methods[0])

        assert ride.unpaid_price == 125
        assert passenger.current_ride_id == ride.id
        assert passenger.is_payed is False

    def test_full_payment_clears_current_ride(self, passenger_with_ride):
        passenger, ride = passenger_with_ride
        complete_ride(ride)

        passenger.pay_ride(ride.total_price, passenger.payment_methods[0])

        assert ride.is_payed is True
        assert passenger.is_payed is True
        assert passenger.current_ride_id is None

    def test_register_payment_method(self):
        passenger = Passenger('Passenger One', 9876543210)
        method = Cash()

        passenger.register_payment_method(method)

        assert passenger.payment_methods == [None, None, None, method]

    # Invalid inputs
    @pytest.mark.parametrize('phone_number', ['9876543210', 123, 12345678901])
    def test_invalid_phone_number(self, phone_number):
        with pytest.raises(ValueError):
            Passenger('Passenger One', phone_number)

    def test_invalid_name(self):
        with pytest.raises(ValueError):
            Passenger(123, 9876543210)

    def test_ride_requires_a_payment_method(self):
        passenger = Passenger('Passenger One', 9876543210)

        with pytest.raises(ValueError, match='payment method'):
            passenger.make_ride_request('Istanbul', 'Bursa', 1, 'standart_car', 10)

    def test_payment_method_must_belong_to_passenger(self, passenger_with_ride):
        passenger, ride = passenger_with_ride
        complete_ride(ride)

        with pytest.raises(ValueError, match="isn't yours"):
            passenger.pay_ride(200, Cash())

    def test_only_payment_instances_can_be_registered(self):
        passenger = Passenger('Passenger One', 9876543210)

        with pytest.raises(TypeError, match='must be a Payment'):
            passenger.register_payment_method(object())

    def test_duplicate_payment_type_is_rejected(self):
        passenger = Passenger('Passenger One', 9876543210, cash_method=Cash())

        with pytest.raises(ValueError, match='already have'):
            passenger.register_payment_method(Cash())

    def test_payment_requires_completed_ride(self, passenger_with_ride):
        passenger, _ = passenger_with_ride

        with pytest.raises(ValueError, match='complete the ride'):
            passenger.pay_ride(200, passenger.payment_methods[0])

    # Edge cases
    def test_cancelling_ride_clears_passenger_and_releases_driver(
        self, passenger_with_ride
    ):
        passenger, ride = passenger_with_ride

        passenger.cancell_ride()

        assert ride.status == 'Cancelled'
        assert passenger.current_ride_id is None
        assert DriverRegistry.find_available('standart_car') is not None

    def test_view_ride_history_displays_saved_ride(self, passenger_with_ride, capsys):
        passenger, _ = passenger_with_ride

        passenger.view_ride_history()

        output = capsys.readouterr().out
        assert 'Passenger Passenger One history' in output
        assert 'Pickup: Istanbul' in output

        