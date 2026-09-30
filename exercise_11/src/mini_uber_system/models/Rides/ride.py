class Ride:
    _ride_items = {}
    id = 1


    @classmethod
    def register_ride_item(cls, ride_item):
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