from ..Vehicles.vehicle import Vehicle


class RideItem:
    def __init__(self, pickup_location, destination, num_of_passengers, vehicle_type, distance, passenger):
        self.pickup_location = pickup_location
        self.destination = destination
        self.num_of_passengers = num_of_passengers
        self.vehicle_type = vehicle_type
        self.passenger = passenger

        self.distance = distance
        prices = Vehicle.get_vehicle_prices(vehicle_type)
        self.base_fare = prices['base_fare']
        self.price_per_kilometer = prices['price_per_kilometer']
        self.total_price = self.base_fare + self.price_per_kilometer * self.distance
        self.unpaid_price = self.total_price
        self.status = 'Requested'
        self.is_payed = False

        from .ride import Ride

        self.id = Ride.register_ride_item(self)

    @classmethod
    def find_ride_item(cls, ride_item_id):
        from .ride import Ride

        return Ride.get_ride_item(ride_item_id)


    def accept_ride(self):
        if self.status != 'Requested':
            raise ValueError(f"you can't accept ride {self.id} if it's status isn't Requested")

        self.status = 'Accepted'


    def start_ride(self):
        if self.status != 'Accepted':
            raise ValueError(f"you can't start ride {self.id} if it's status isn't Accepted")

        self.status = 'In_Progress' 


    def complete_ride(self):
        if self.status != 'In_Progress':
            raise ValueError(f"you can't start ride {self.id} if it's status isn't In_Progress")

        self.status = 'Completed'      


    def cancell_ride(self):
        if self.status != 'Requested' or self.status != 'Accepted':
            raise ValueError(f"you can't cancell ride {self.id} in this state")

        self.status = 'Cancelled'


    def display(self):
        print(f"Passenger: {self.passenger.name}")
        print(f"Pickup: {self.pickup_location}")
        print(f"Destination: {self.destination}")
        print(f"Passengers: {self.num_of_passengers}")
        print(f"Vehicle Type: {self.vehicle_type}")


