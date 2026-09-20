class OrderItem:
    def __init__(self, product, quantity):
        self._locked = False

        if quantity <= 0:
            raise ValueError(
                "ordered item's quantity must be greater than zero"
            )

        
        if product.quantity < quantity:
            raise ValueError(
                f"not enough stock for {product.name}"
            )

        
        self.product = product
        self._price = product.price
        self._quantity = quantity


    # setters
    def price_setter(self, price):
        if self._locked:
            raise ValueError("paid order items cannot be changed")
        if price < 0:
            raise ValueError("price can't be negative")
        self._price = price

    def quantity_setter(self, quantity):
        if self._locked:
            raise ValueError("paid order items cannot be changed")
        if quantity <= 0:
            raise ValueError(
                "ordered item's quantity must be greater than zero"
            )
        self._quantity = quantity

    def _lock(self):
        self._locked = True


    # getters
    def price_getter(self):
        return self._price

    def quantity_getter(self):
        return self._quantity

    
    price = property(
        fset=price_setter,
        fget=price_getter
    )
    
    quantity = property(
        fset=quantity_setter,
        fget=quantity_getter
    )