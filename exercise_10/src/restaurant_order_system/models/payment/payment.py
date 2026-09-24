from abc import abstractmethod, ABC

class Payment(ABC):
    @abstractmethod
    def pay(self, order):
        if order.is_paid:
            raise ValueError("you can't pay an already paid order")    
        if order.status == 'Cancelled':
            raise ValueError("you can't pay a cancelled order")
        if not order.menu_items or order.final_total <= 0:
            raise ValueError("the order total must be greater than zero")