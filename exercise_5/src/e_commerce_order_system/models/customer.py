class Customer:
    def __init__(self, name, customer_id, email):
        if customer_id < 0:
            raise ValueError("customer id can't be negative")

        self.name = name
        self.customer_id = customer_id
        self.email = email
        self._orders = []

    @property
    def orders(self):
        return self._orders