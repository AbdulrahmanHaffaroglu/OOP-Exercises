from abc import ABC

_VEHICLE_PRICES = {
    'standart_car': {'base_fare': 50, 'price_per_kilometer': 15},
    'premium_car': {'base_fare': 100, 'price_per_kilometer': 25},
    'motorcycle': {'base_fare': 30, 'price_per_kilometer': 10},
}

class Vehicle(ABC):

    _vehicle_items = {}
    id = 1
    
    def __init__(self, max_passengers: int, base_fare, price_per_kilometer, vehicle_type):
        if max_passengers <= 0:
            raise ValueError("this is not a valid number of passengers")
        
        if base_fare < 0 or price_per_kilometer < 0:
            raise ValueError("we can't have negative value in charges")

        if base_fare == 0 and price_per_kilometer == 0:
            raise ValueError("we can't charge the passenger 0 tl")

        self.id = Vehicle.id
        Vehicle.id += 1
        Vehicle._vehicle_items[self.id] = self

        self.max_passengers = max_passengers
        self.base_fare = base_fare
        self.price_per_kilometer = price_per_kilometer
        self.vehicle_type = vehicle_type


    @classmethod
    def create_vehicle(cls, vehicle_type):
        return VehicleFactory.create_vehicle(vehicle_type)


    @classmethod
    def get_vehicle_prices(cls, vehicle_type):
        try:
            return _VEHICLE_PRICES[vehicle_type].copy()
        except KeyError:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}") from None


    @classmethod
    def get_max_passengers(cls, vehicle_type):
        if vehicle_type == 'standart_car':
            return 4

        elif vehicle_type == 'premium_car':
            return 4
        
        elif vehicle_type == 'motorcycle':
            return 1

        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}") 

    @classmethod
    def get_vehicle(cls, vehicle_id):
        try:
            return cls._vehicle_items[vehicle_id]
        except KeyError:
            raise ValueError(f"this id {vehicle_id} does not exist")



class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        from .motorcycle import Motorcycle
        from .premium_car import PremiumCar
        from .standart_car import StandartCar

        if vehicle_type == 'standart_car':
            vehicle_class = StandartCar
            max_passengers = 4

        elif vehicle_type == 'premium_car':
            vehicle_class = PremiumCar
            max_passengers = 4
        
        elif vehicle_type == 'motorcycle':
            vehicle_class = Motorcycle
            max_passengers = 1
        
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")

        prices = Vehicle.get_vehicle_prices(vehicle_type)
        return vehicle_class(
            max_passengers,
            prices['base_fare'],
            prices['price_per_kilometer'],
            vehicle_type,
        )