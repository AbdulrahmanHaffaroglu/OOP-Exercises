from Vehicles.vehicle import Vehicle
from .ride import Ride

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

        self.id = Ride.register_ride_item(self)
        Ride.assign(self)


    @classmethod
    def find_ride_item(ride_item_id):
        return Ride.get_ride_item(ride_item_id)


    def display(self):
        print(f"Passenger: {self.passenger.name}")
        print(f"Pickup: {self.pickup_location}")
        print(f"Destination: {self.destination}")
        print(f"Passengers: {self.num_of_passengers}")
        print(f"Vehicle Type: {self.vehicle_type}")