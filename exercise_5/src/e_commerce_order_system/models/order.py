from .order_item import OrderItem 

class Order:

    valid_status = [
        "pending",
        "paid",
        "shipped",
        "cancelled"
    ]

    def __init__(self, order_id, customer):

        if order_id < 0:
            raise ValueError("order id can't be negative")

        self.order_id = order_id
        self._order_items = []
        self._status = "pending"
        self.customer = customer

        customer._orders.append(self)

    @property
    def status(self):
        return self._status

    @property
    def order_items(self):
        return tuple(self._order_items)

    def add_product(self, product, quantity):

        if self._status == "paid":
            raise ValueError("paid orders cannot be changed")

        if self._status in ["shipped", "cancelled"]:
            raise ValueError(
                "shipped or cancelled orders cannot be changed"
            )

        # Prevent the same product from appearing twice
        for item in self._order_items:
            if item.product is product:
                raise ValueError(
                    "the product already exists in this order"
                )

        item = OrderItem(product, quantity)
        self._order_items.append(item)

    def del_product(self, product):

        if self._status == "paid":
            raise ValueError("paid orders cannot be changed")

        if self._status in ["shipped", "cancelled"]:
            raise ValueError(
                "shipped or cancelled orders cannot be changed"
            )

        for item in self._order_items:
            if item.product is product:
                self._order_items.remove(item)
                return

        raise ValueError("product is not in this order")

    def total_price(self):
        return sum(
            item.price * item.quantity
            for item in self._order_items
        )

    def change_status(self, status):

        if status not in self.valid_status:
            raise ValueError("this is not a valid status")

        # Same status
        if self._status == status:
            return

        # Shipped orders cannot be cancelled
        if self._status == "shipped" and status == "cancelled":
            raise ValueError("shipped orders cannot be cancelled")

        # Cancelled orders cannot be paid
        if self._status == "cancelled" and status == "paid":
            raise ValueError("cancelled orders cannot be paid")

        # Paid orders cannot go back to pending
        if self._status == "paid" and status == "pending":
            raise ValueError("paid orders cannot return to pending")

        # Shipped orders cannot go backwards
        if self._status == "shipped":
            raise ValueError("shipped orders cannot change status")

        # Pay the order
        if status == "paid":

            # First verify ALL products have enough stock.
            # This prevents partially changing the stock.
            for item in self._order_items:
                if item.product.quantity < item.quantity:
                    raise ValueError(
                        f"not enough stock for {item.product.name}"
                    )

            # Only modify stock after all checks succeed.
            for item in self._order_items:
                item.product.decrease_stock(item.quantity)
                item._lock()

        # Cancel a paid order and restore its stock
        if self._status == "paid" and status == "cancelled":

            for item in self._order_items:
                item.product.increase_stock(item.quantity)

        self._status = status