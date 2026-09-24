from .order_item import OrderItem

class Order:
    orders_list = []

    @classmethod
    def add_order(cls, customer, menu_items):
        order = OrderItem(customer, menu_items)
        cls.orders_list.append(order)
        return order

    @classmethod
    def remove_order(cls, order_item):
        if order_item.status == 'Cancelled':
            raise ValueError("you already cancelled this order")

        if order_item.status not in ('Pending', 'Confirmed'):
            raise ValueError("you can't cancel this order")
        
        order_item.status = 'Cancelled'
        





