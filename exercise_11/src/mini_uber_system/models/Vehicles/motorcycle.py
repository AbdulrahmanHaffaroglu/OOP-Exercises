from .vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, max_passengers, base_fare, price_per_kilometer, vehicle_type):
        super().__init__(max_passengers, base_fare, price_per_kilometer, vehicle_type)