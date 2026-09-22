from vehicle_system.models.car import Car
from vehicle_system.models.motorcycle import Motorcycle
from vehicle_system.models.register import Register
from vehicle_system.models.truck import Truck


def main():
   """Demonstrate registration, trips, fuel consumption, and details."""
   Register.registered_vehicles.clear()

   vehicles = [
      Car("Toyota", "Corolla", 5),
      Motorcycle("Honda", "CBR", 600),
      Truck("FH", "Volvo", 20),
   ]

   for vehicle in vehicles:
      Register.add(vehicle)
      vehicle.refuel(20)
      vehicle.start_vehicle()
      vehicle.start_trip()
      vehicle.finish_trip()
      vehicle.stop_vehicle()
      vehicle.show_details()
      print()


if __name__ == "__main__":
   main()