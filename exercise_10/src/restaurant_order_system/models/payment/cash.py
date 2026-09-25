from .payment import Payment

class Cash(Payment):
    def __init__(self, customer):
        customer.cash_method = self
        customer.register_payment_method(self)

    def pay(self, order, succeeds=True):
        super().pay(order)
        if not succeeds:
            print("Payment failed.")
            return False
        print("Waiting for cash payment...")
        print("Payment received.")
        order.mark_paid(self)
        return True