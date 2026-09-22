from .vehicle import Vehicle
from vehicle_system.utils import generate_id

class Truck(Vehicle):
    id_num = 0
    trip_fuel = 10

    def __init__(self, model, brand, cargo_storage):
        super().__init__(model, brand)
        self.cargo_storage = cargo_storage


    def make_id(self):
        id = generate_id(Truck.id_num, 'TRUCK')
        Truck.id_num += 1
        return id

    def start_vehicle(self):
        super().start_vehicle()

        print("Starting truck...")
        print("Checking engine system...")
        print("Checking air pressure...")
        print("Engine started.")
        print("Running")

    def stop_vehicle(self):
        super().stop_vehicle()

        print("The truck is slowing...")
        print("Air pressure reducing...")
        print("Engine stopped.")
        print("Stopped")

    def start_trip(self):
        super().start_trip()

    def finish_trip(self):
        super().finish_trip()

        print("trip for truck finished")

    def refuel(self, amount):
        return super().refuel(amount)

    def show_details(self):
        super().show_details()
        print(f"Cargo storage: {self.cargo_storage}")