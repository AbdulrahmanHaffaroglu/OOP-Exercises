from abc import ABC, abstractmethod

class Payment(ABC):

    @ abstractmethod
    def pay(self, ride_item, amount):
        if amount <= 0:
            raise ValueError("you can't pay 0 or a negative amount")