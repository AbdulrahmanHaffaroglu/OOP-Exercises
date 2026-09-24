from .order_line import OrderLine

class OrderItem():

    id_num = 0

    def __init__(self, customer, menu_items=None):

        self.customer = customer
        self.status = 'Pending'
        self.menu_items = []
        self.id = f"{OrderItem.id_num:03d}"
        self.is_paid = False 
        self.discount = None
        self.discount_amount = 0
        self.payment_method = None
        self.paid_total = None
        OrderItem.id_num += 1

        for menu_item in menu_items or []:
            self.add_item(menu_item)

    def add_item(self, menu_item, quantity=1, options=None):
        self._ensure_editable()

        if quantity <= 0:
            raise ValueError("quantity must be greater than zero")

        if not menu_item.is_available:
            raise ValueError("this item is not available")

        for order_line in self.menu_items:
            if order_line.matches(menu_item, options):
                order_line.quantity += quantity
                return

        self.menu_items.append(OrderLine(menu_item, quantity, options))

    def remove_item(self, menu_item, options=None):
        self._ensure_editable()

        for order_line in self.menu_items:
            if order_line.matches(menu_item, options):
                self.menu_items.remove(order_line)
                return

        raise ValueError("this item is not in your order")
        
    def increase_quantity(self, menu_item, amount, options=None):
        self._ensure_editable()
        if amount <= 0:
            raise ValueError("quantity must be greater than zero")

        for order_line in self.menu_items:
            if order_line.matches(menu_item, options):
                order_line.quantity += amount
                return

        raise ValueError("you don't have this item in this order")

        
    def decrease_quantity(self, menu_item, amount, options=None):
        self._ensure_editable()
        if amount <= 0:
            raise ValueError("quantity must be greater than zero")

        for order_line in self.menu_items:
            if order_line.matches(menu_item, options):
                if order_line.quantity - amount <= 0:
                    raise ValueError("you can't reduce the quantity of an item to zero or below")
                order_line.quantity -= amount
                return

        raise ValueError("you don't have this item in this order") 

        
    def order_status(self):
        print(self.status)
        return self.status

    @property
    def total_price(self):
        return sum(order_line.total_price for order_line in self.menu_items)

    def show_total(self):
        total = self.final_total

        print(f"total for Order-{self.id}: {total}")
        return total

    @property
    def final_total(self):
        if self.paid_total is not None:
            return self.paid_total
        return max(0, self.total_price - self.discount_amount)

    def apply_discount(self, discount):
        if self.is_paid:
            raise ValueError("you can't change the discount on a paid order")
        if not self.menu_items:
            raise ValueError("you can't discount an empty order")

        self.discount = discount
        self.discount_amount = discount.calculate(self.total_price)
        return self.final_total

    def mark_paid(self, payment_method):
        self.is_paid = True
        self.payment_method = payment_method
        self.paid_total = self.final_total

    def summary(self):
        return {
            "id": self.id,
            "customer": self.customer.name if self.customer else None,
            "items": [
                {
                    "name": line.menu_item.name,
                    "quantity": line.quantity,
                    "total": line.total_price,
                    "options": [option.name for option in line.options],
                }
                for line in self.menu_items
            ],
            "subtotal": self.total_price,
            "discount": self.discount_amount,
            "final_total": self.final_total,
            "payment": type(self.payment_method).__name__ if self.payment_method else None,
            "payment_status": "Paid" if self.is_paid else "Unpaid",
            "order_status": self.status,
        }

    def _ensure_editable(self):
        if self.status not in ('Pending', 'Confirmed'):
            raise ValueError("you can't modify this order anymore")
        if self.is_paid:
            raise ValueError("you can't change a paid order")