class PercentageDiscount:
    def __init__(self, percentage):
        if not 0 < percentage <= 100:
            raise ValueError("percentage must be greater than 0 and at most 100")
        self.percentage = percentage

    def calculate(self, subtotal):
        return subtotal * self.percentage / 100


class FixedDiscount:
    def __init__(self, amount):
        if amount <= 0:
            raise ValueError("discount amount must be greater than zero")
        self.amount = amount

    def calculate(self, subtotal):
        return min(self.amount, subtotal)