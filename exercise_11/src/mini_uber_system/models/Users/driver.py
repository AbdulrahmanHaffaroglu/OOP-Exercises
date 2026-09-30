from .user import User
from .driver_registry import DriverRegistry
from ..Rides.ride_item import RideItem

class Driver(User):
    def __init__(self, name, phone_number, vehicle=None):

        self.current_ride_id = None
        
        id = DriverRegistry.register_driver(self)
        self.status = 'Available'
        super().__init__(id, name, phone_number, [], self.current_ride_id)
        self.vehicle_id = None
        self.vehicle_type = None

        if vehicle:
            self.register_vehicle(vehicle)


    def register_vehicle(self, vehicle):
        if self.vehicle_id:
           raise ValueError("you already registered a vehicle")

        self.vehicle_id = vehicle.id
        self.vehicle_type = vehicle.vehicle_type 


    def change_status(self, new_status):
        if new_status == self.status:
            raise ValueError(f"driver is already {new_status}")

        self.status = new_status


    def accept_ride(self, ride_item):

        if not self.vehicle_id:
            raise ValueError("you should register a vehicle before tarting to accept rides")

        if self.vehicle_type != ride_item.vehicle_type:
            raise ValueError("you can't accept this ride request now")

        if self.current_ride_id:
            raise ValueError("you already have currently a ride")

        self.change_status('Busy') # this also checks that the driver isn't currently busy
        ride_item.accept_ride()
        self.current_ride_id = ride_item.id
        self.ride_history.append(ride_item.id)


    def start_ride(self):
        ride = RideItem.find_ride_item(self.current_ride_id)

        ride.start_ride()


    def complete_ride(self):
        ride_item = RideItem.find_ride_item(self.current_ride_id)

        ride_item.complete_ride()
        self.change_status('Active')

        print(f"the total price for ride {ride_item.id} is: {ride_item.total_price}")
        self.current_ride_id = None


    @classmethod
    def find_available_driver(cls, vehicle_type):
        return DriverRegistry.find_available(vehicle_type)
    

    def view_current_ride(self):
        super().view_current_ride()


    def view_ride_history(self):
        print(f"Driver {self.name} history:")
        print("---------")
        super().view_ride_history()