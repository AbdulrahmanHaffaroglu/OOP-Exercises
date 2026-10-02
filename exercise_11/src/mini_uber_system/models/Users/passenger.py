from .user import User
from ..Rides.ride_item import RideItem
from .driver_registry import DriverRegistry

class Passenger(User):

    id_num = 1

    def __init__(self, name, phone_number, cash_method=None, bank_transfer_method=None, credit_card_method=None):

        self.current_ride_id = None
        
        id = f"driver-{Passenger.id_num:03d}"
        Passenger.id_num += 1
        
        super().__init__(id, name, phone_number, [], self.current_ride_id)
        
        self.payment_methods = [cash_method, bank_transfer_method, credit_card_method]
        self.is_payed = False


    def make_ride_request(self, pickup_location, destination, num_of_passengers, vehicle_type, distance):

        if self.current_ride_id:
            raise ValueError("you can't have more than one ride request")

        if all( method is None for method in self.payment_methods ):
            raise ValueError("you should have at least one payment method before making a ride request")


        ride_item = RideItem(pickup_location, 
                            destination, 
                            num_of_passengers, 
                            vehicle_type, 
                            distance, 
                            self)
            
        self.current_ride_id = ride_item.id
        self.ride_history.append(ride_item.id) 
        self.is_payed = False

        return ride_item


    def cancell_ride(self):
        if self.current_ride_id == None:
            raise ValueError("you currently don't have a Active ride to cancell")

        ride_item = RideItem.find_ride_item(self.current_ride_id)

        ride_item.cancell_ride()

        for driver in DriverRegistry.drivers.values():
            if driver.current_ride_id == self.current_ride_id:
                driver.change_status('Available')
                driver.current_ride_id = None

        self.current_ride_id = None


    def pay_ride(self, amount, payment_method):
        if self.current_ride_id == None:
            raise ValueError("you don't have a active ride to pay right now")
        
        if payment_method not in self.payment_methods:
            raise ValueError("this payment method isn't yours")

        ride_item = RideItem.find_ride_item(self.current_ride_id)

        if ride_item.status == 'Cancelled':
            raise ValueError("you already cancelled this ride")

        if ride_item.status != 'Completed':
            raise ValueError("you should complete the ride before you can pay for it")

        self.is_payed = payment_method.pay(ride_item, amount)
        ride_item.is_payed = self.is_payed

        if self.is_payed:
            self.current_ride_id = None


    def register_payment_method(self, payment_method):
        from ..Payment_Methods.payment import Payment

        if not isinstance(payment_method, Payment):
            raise TypeError("payment_method must be a Payment")

        if any(
            registered_method is not None
            and type(registered_method) is type(payment_method)
            for registered_method in self.payment_methods
        ):
            raise ValueError("you already have a payment method of this type")

        self.payment_methods.append(payment_method)


    def view_current_ride(self):
        super().view_current_ride()


    def view_ride_history(self):
        print(f"Passenger {self.name} history:")
        print("---------")
        super().view_ride_history()