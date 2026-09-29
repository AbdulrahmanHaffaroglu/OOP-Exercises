from abc import abstractmethod, ABC
from ..Rides.ride_item import RideItem

class User(ABC):

    @abstractmethod
    def __init__(self, id, name, phone_number, ride_history, current_ride_id):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.ride_history = ride_history
        self.current_ride_id = current_ride_id


    @abstractmethod
    def view_current_ride(self):
        ride = RideItem.find_ride_item(self.current_ride_id)

        ride.display()


    @abstractmethod
    def view_ride_history(self):
        for ride_id in self.ride_history:
            ride = RideItem.find_ride_item(ride_id)

            ride.display()