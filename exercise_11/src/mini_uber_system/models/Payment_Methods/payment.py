from abc import ABC, abstractmethod

class Payment(ABC):

    @ abstractmethod
    def pay(self, ride_item, amount):
        pass