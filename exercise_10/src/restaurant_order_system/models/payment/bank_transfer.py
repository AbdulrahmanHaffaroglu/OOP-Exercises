from .payment import Payment

class BankTransfer(Payment):
    def __init__(self, customer):
        customer.bank_transfer_method = self
        customer.register_payment_method(self)
        self.discount = None


    def pay(self, order, succeeds=True):
        super().pay(order)
        if not succeeds:
            print("Payment failed.")
            return False
        print("Checking bank transfer...")
        print("Transfer confirmed.")
        order.mark_paid(self)
        return True