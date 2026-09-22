from .vehicle import Vehicle
from vehicle_system.utils import generate_id

class Motorcycle(Vehicle):

    id_num = 0
    trip_fuel = 3

    def __init__(self, brand, model, engine_cc):
        super().__init__(model, brand)
        self.engine_cc = engine_cc

    def make_id(self):
        id = generate_id(Motorcycle.id_num, 'MOTOR')
        Motorcycle.id_num += 1
        return id

    def start_vehicle(self):
        super().start_vehicle()

        print("Starting motorcycle...")
        print("Engaging starter...")
        print("Checking air pressure...")
        print("Engine started.")
        print("Running")

    def stop_vehicle(self):
        super().stop_vehicle()

        print("The motor is slowing...")
        print("Engine stopped.")
        print("Stopped")

    def start_trip(self):
        super().start_trip()

    def finish_trip(self):
        super().finish_trip()

        print("trip for motorcycle finished")

    def refuel(self, amount):
        return super().refuel(amount)

    def show_details(self):
        super().show_details()
        print(f"Engine capacity: {self.engine_cc}cc")