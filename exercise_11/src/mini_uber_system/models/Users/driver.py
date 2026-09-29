from .user import User
from .driver_registry import DriverRegistry
from ..Rides.ride_item import RideItem

class Driver(User):
    def __init__(self, name, phone_number, vehicle):

        self.current_ride_id = None
        
        super().__init__(id, name, phone_number, self.current_ride_id, ride_history=[])
        self.status = 'Available'
        self.vehicle_id = vehicle.id
        self.vehicle_type = vehicle.vehicle_type
        id = DriverRegistry.register_driver(self)


    def change_status(self, new_status):
        if new_status == self.status:
            raise ValueError(f"driver is already {new_status}")

        self.status = new_status


    def accept_ride(self, ride_item):
        if self.status == 'Busy':
            raise ValueError("you can't accept ride while you are busy")

        if self.vehicle_type != ride_item.vehicle_type:
            raise ValueError("you can't accept this ride request now")

        ride_item.accept_ride()
        self.current_ride_id = ride_item.id
        self.change_status('Busy')


    def start_ride(self):
        ride = RideItem.find_ride_item(self.current_ride_id)

        ride.accept_ride()


    def complete_ride(self):
        ride = RideItem.find_ride_item(self.current_ride_id)

        ride.complete_ride()
        self.change_status('Active')
        
        self.current_ride_id = None


    @classmethod
    def find_available_driver(cls, vehicle_type):
        return DriverRegistry.find_available(vehicle_type)
    

    def view_current_ride(self):
        super().view_current_ride()


    def view_ride_history(self):
        super().view_current_ride()