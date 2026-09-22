from .vehicle import Vehicle
from vehicle_system.utils import generate_id

class Car(Vehicle):

    id_num = 0
    trip_fuel = 5

    def __init__(self, brand, model, max_passengers):
        super().__init__(model, brand)
        self.max_passengers = max_passengers


    def make_id(self):
        id = generate_id(Car.id_num, 'CAR')
        Car.id_num += 1
        return id

    def start_vehicle(self):
        super().start_vehicle()

        print("Starting car...")
        print("Checking ignition...")
        print("Engine started.")
        print("Running")

    def stop_vehicle(self):
        super().stop_vehicle()

        print("The car is slowing...")
        print("Engine stopped.")
        print("Stopped")
        
    def start_trip(self):
        super().start_trip()

    def finish_trip(self):
        super().finish_trip()

        print("trip for car finished")

    def refuel(self, amount):
        return super().refuel(amount)

    def show_details(self):
        super().show_details()
        print(f"Max passengers: {self.max_passengers}")