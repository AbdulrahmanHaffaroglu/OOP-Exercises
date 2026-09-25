from .payment import Payment

class CreditCard(Payment):
    def __init__(self, customer):
        customer.credit_card_method = self
        customer.register_payment_method(self)

    def pay(self, order, succeeds=True):
        super().pay(order)
        if not succeeds:
            print("Payment failed.")
            return False
        print("Checking card...")
        print("Processing payment...")
        print("Payment successful.")
        order.mark_paid(self)
        return True
