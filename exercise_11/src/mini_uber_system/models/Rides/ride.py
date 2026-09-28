from Users.driver import Driver

class Ride:
    _ride_items = {}
    id = 1


    @classmethod
    def check_for_available_drivers(cls, vehicle_type):
        available_drivers = Driver.find_available_driver(vehicle_type)

        if available_drivers is None:
            raise ValueError("there is no available rider that can take the request")


    @classmethod
    def register_ride_item(cls, ride_item):
        Ride.check_for_available_drivers(cls, ride_item.vehicle_type)
        ride_id = cls.id
        cls.id += 1
        cls._ride_items[ride_id] = ride_item
        return ride_id


    @classmethod
    def get_ride_item(cls, ride_id):
        try:
            return cls._ride_items[ride_id]
        except KeyError:
            raise ValueError(f"No ride found with ID {ride_id}") from None
