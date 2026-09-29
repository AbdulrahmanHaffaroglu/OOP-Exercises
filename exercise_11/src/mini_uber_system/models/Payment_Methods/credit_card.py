from .payment import Payment

class CreditCard(Payment):
    def pay(self, ride_item, amount):
        super().__init__(ride_item, amount)

        if amount <= ride_item.unpaid_price:
            ride_item.unpaid_price -= amount
            
        else:
           ride_item.unpaid_price -= amount
           print("you paid using Credit Card")
           print(f"you paid more than the total price, we returned {amount - ride_item.unpaid_price}")

        print("you paid using Credit Card")

        if ride_item.unpaid_price == 0:
            print("you paid all your debt")
            return True
            
        elif ride_item.unpaid_price > 0:
            print(f"you still have {ride_item.unpaid_price} tl to pay")
            return False

        