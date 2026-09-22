from .car import Car
from .truck import Truck
from .motorcycle import Motorcycle

class Register:

    registered_vehicles = []

    @classmethod
    def add(cls, vehicle: Motorcycle | Car | Truck):

        if vehicle in cls.registered_vehicles:
            raise ValueError("this vehicle is already registered")

        if vehicle.id is not None:
            raise ValueError("this vehicle is already registered")

        vehicle.id = vehicle.make_id()

        cls.registered_vehicles.append(vehicle)

    @classmethod
    def remove(cls, vehicle):
        cls.registered_vehicles.remove(vehicle)
        vehicle.id = None