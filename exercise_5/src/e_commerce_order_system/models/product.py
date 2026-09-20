class Product:
    def __init__(self, product_id, name, price, quantity):
        if price < 0:
            raise ValueError("price can't be negative")

        if quantity < 0:
            raise ValueError("quantity can't be negative")

        if product_id < 0:
            raise ValueError("product id can't be negative")

        self.product_id = product_id
        self.name = name
        self._price = price
        self._quantity = quantity

    # Getter functions
    def quantity_getter(self):
        return self._quantity

    def price_getter(self):
        return self._price

    # Setter functions
    def quantity_setter(self, quantity):
        if quantity < 0:
            raise ValueError("quantity can't be negative")

        self._quantity = quantity

    def price_setter(self, price):
        if price < 0:
            raise ValueError("price can't be negative")

        self._price = price

    # Stock functions
    def increase_stock(self, amount):
        if amount < 0:
            raise ValueError(
                "you can't increase the stock with a negative amount"
            )

        self._quantity += amount

    def decrease_stock(self, amount):
        if amount < 0:
            raise ValueError(
                "you can't decrease the stock with a negative amount"
            )

        if self._quantity < amount:
            raise ValueError("stock quantity shouldn't become negative")

        self._quantity -= amount

    quantity = property(
        fget=quantity_getter,
        fset=quantity_setter
    )

    price = property(
        fget=price_getter,
        fset=price_setter
    )