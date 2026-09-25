from .the_menu.menu_item import MenuItem
from .orders.order import OrderItem, Order
from .payment.bank_transfer import BankTransfer
from .payment.cash import Cash
from .payment.credit_card import CreditCard

class Customer:
    num = 0

    def __init__(self, name, contact_information, cash_method=None, credit_card_method=None, bank_transfer_method=None):
        self.name = name
        self.contact_information = contact_information
        self.id = f"{Customer.num:03d}"
        self.cash_method = cash_method
        self.credit_card_method = credit_card_method
        self.bank_transfer_method = bank_transfer_method
        self.payment_methods = []
        for payment_method in (cash_method, bank_transfer_method, credit_card_method):
            if payment_method is not None:
                self.register_payment_method(payment_method)

        Customer.num += 1

        self.orders = []


    def create_order(self, menu_items): 
        order = Order.add_order(self, menu_items)
        self.orders.append(order)
        return order


    def cancel_order(self, order):
        if order not in self.orders:
            raise ValueError("you don't have this order")

        Order.remove_order(order)


    def view_orders(self):
        return [order.summary() for order in self.orders]


    def add_item(self, menu_item, order_item, quantity=1, options=None):
        if quantity <= 0:
            raise ValueError("you should want at least one of an item")
        
        if order_item not in self.orders:
            raise ValueError("you dont have this order")

        if menu_item.is_available == False:
            raise ValueError("this item is not available")

        order_item.add_item(menu_item, quantity, options)


    def remove_item(self, menu_item, order_item: OrderItem, options=None):
        if order_item not in self.orders:
            raise ValueError("you don't have this order")

        order_item.remove_item(menu_item, options)

        
    def increase_quantity(self, order_item: OrderItem, menu_item, amount, options=None):
        if order_item not in self.orders:
            raise ValueError("you don't have this order")

        if amount <= 0:
            raise ValueError("you should increase the amount by one or more")
        
        order_item.increase_quantity(menu_item, amount, options)


    def reduce_quantity(self, order_item: OrderItem, menu_item, amount, options=None):
        if order_item not in self.orders:
            raise ValueError("you don't have this order")
        
        order_item.decrease_quantity(menu_item, amount, options)


    def check_order_status(self, order: OrderItem): 
        if order not in self.orders:
            raise ValueError("you don't have this order")
        return order.order_status()

    def register_payment_method(self, payment_method):
        if payment_method not in self.payment_methods:
            self.payment_methods.append(payment_method)


    def pay_order(self, order_item, payment_method: Cash | CreditCard | BankTransfer, succeeds=True):
        if order_item not in self.orders:
            raise ValueError("you don't have this order")


        if not order_item.menu_items:
            raise ValueError("this order is empty")

        if order_item.status == 'Cancelled':
            raise ValueError("this order is already cancelled")

        if payment_method is None or payment_method not in self.payment_methods:
            raise ValueError("you don't own this payment method")
         
        result = payment_method.pay(order_item, succeeds)
        print(f"total for Order-{order_item.id}: {order_item.final_total}")
        return result

    def apply_discount(self, order_item, discount):
        if order_item not in self.orders:
            raise ValueError("you don't have this order")
        return order_item.apply_discount(discount)


    def order_total(self, order):
        if order not in self.orders:
            raise ValueError("this order is not yours")

        return order.show_total()