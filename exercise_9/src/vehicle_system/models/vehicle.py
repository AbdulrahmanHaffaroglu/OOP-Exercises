from abc import ABC
from vehicle_system.utils import all_abstract
from .engine import Engine

@all_abstract
class Vehicle(ABC):
    def __init__(self, model, brand):
        self.id = None
        self.status = 'Stopped'
        self.engine = Engine()
        self.brand = brand
        self.model = model
        self.fuel = 0
        self.on_trip = False


    def make_id(self): pass

    def start_vehicle(self):
        if self.id is None:
            raise ValueError("register this vehicle in order to use it")

        if self.fuel == 0:
            raise ValueError("you can't start an empty vehicle")

        if self.status != 'Stopped':
            raise ValueError("you can't start a vehicle that is already running")

        self.engine.start()
        self.status = 'Running'

    def stop_vehicle(self): 
        if self.id is None:
            raise ValueError("register this vehicle in order to use it")

        if self.status == 'Stopped':
            raise ValueError("you can't stop a already stopped vehicle")

        if self.on_trip:
            raise ValueError("you can't stop a vehicle during a trip")

        self.engine.stop()
        self.status = 'Stopped'


    def start_trip(self):
        if self.status != "Running":
            raise ValueError("you can only start a trip with a running vehicle")

        if self.on_trip:
            raise ValueError("you can't start another trip while already on a trip")

        if self.fuel < self.trip_fuel:
            raise ValueError("you don't have enough fuel")

        self.on_trip = True
        self.status = "On trip"

    def finish_trip(self):
        if not self.on_trip:
            raise ValueError("you can't finish a trip that hasn't started")

        self.fuel -= self.trip_fuel
        self.on_trip = False
        self.status = "Running"

    def refuel(self, amount):
        if self.status == 'Running':
            raise ValueError("you can't refuel a running vehicle")

        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError("fuel amount must be a number")

        if amount < 0:
            raise ValueError("fuel amount can't be negative")

        if self.fuel + amount > 100:
            self.fuel = 100
            raise ValueError("fuel can't exceed 100%, it's at the maximum now")

        self.fuel += amount
        return self.fuel

    def show_details(self):
        print(f"Vehicle ID: {self.id}")
        print(f"Type: {self.__class__.__name__}")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Fuel: {self.fuel}%")
        print(f"Status: {self.status}")
        print(f"Engine status: {self.engine.status}")