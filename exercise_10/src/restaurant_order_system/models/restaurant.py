from .the_menu.menu import Menu
from .orders.order import Order

class Restaurant:
    def __init__(self):
        self.menu = Menu()

    def add_to_menu(self, menu_item):
        self.menu.add_to_menu(menu_item)

    def remove_from_menu(self, menu_item):
        self.menu.remove_from_menu(menu_item)

    def view_menu(self):
        return self.menu.all_items()

    def find_menu_item(self, item_id):
        return self.menu.find_by_id(item_id)

    def incoming_orders(self):
        menu_items = set(self.menu.menu_items)
        return [
            order
            for order in Order.orders_list
            if order.status == 'Pending'
            and any(line.menu_item in menu_items for line in order.menu_items)
        ]

    @staticmethod
    def confirm_status(order_item, status):
        if order_item.status != status:
            raise ValueError(f"you can't change the order status to {status} right now")

    def confirm_order(self, order_item):
        Restaurant.confirm_status(order_item, 'Pending')

        if order_item.is_paid == False:
            raise ValueError("can't confirm unpaid orders")

        old_status = order_item.status
        order_item.status = 'Confirmed'
        print(f"{old_status} -> {order_item.status}")

    def prepare_order(self, order_item):
        Restaurant.confirm_status(order_item, 'Confirmed')

        old_status = order_item.status
        order_item.status = 'Preparing'
        print(f"{old_status} -> {order_item.status}")

    def ready_order(self, order_item):
        Restaurant.confirm_status(order_item, 'Preparing')

        old_status = order_item.status
        order_item.status = 'Ready'
        print(f"{old_status} -> {order_item.status}")

    def deliver_order(self, order_item):
        Restaurant.confirm_status(order_item, 'Ready')

        old_status = order_item.status
        order_item.status = 'Delivered'
        print(f"{old_status} -> {order_item.status}")