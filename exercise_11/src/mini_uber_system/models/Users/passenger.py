from .user import User
from Rides.ride_item import RideItem
from .driver_registry import DriverRegistry

class Passenger(User):

    id_num = 1

    def __init__(self, name, phone_number, cash_method=None, bank_transfer_method=None, credit_card_method=None):
        
        if all( method is None for method in (cash_method, bank_transfer_method, credit_card_method) ):
            raise ValueError("you don't have any payment method")

        self.current_ride_id = None
        
        id = f"driver-{Passenger.id_num:03d}"
        id_num += 1
        
        super().__init__(id, name, phone_number, self.current_ride_id,  ride_history=[])
        
        self.payment_methods = [cash_method, bank_transfer_method, credit_card_method]



    def make_ride_request(self, pickup_location, destination, num_of_passengers, vehicle_type, distance):
        
        ride = RideItem(pickup_location, 
                        destination, 
                        num_of_passengers, 
                        vehicle_type, 
                        distance, 
                        self)
        
        self.current_ride_id = ride.id
        self.ride_history.append(ride.id) 



    def cancell_ride(self):
        if self.current_ride_id == None:
            raise ValueError("you currently don't have a Active ride to cancell")

        ride = RideItem.find_ride_item(self.current_ride_id)

        if ride.status == 'Requested' or ride.status == 'Accepted':
            raise ValueError("you can't cancell the ride anymore")

        ride.status = 'Cancelled'

        for driver in DriverRegistry.drivers.values():
            if driver.current_ride_id == self.current_ride_id:
                driver.status = 'Available'
                driver.current_ride_id = None

        self.current_ride_id = None

    def view_current_ride(self):
        super().view_current_ride()


    def view_ride_history(self):
        super().view_current_ride()