from .payment import Payment

class BankTransfer(Payment):
    def pay(self, ride_item, amount):
        super().pay(ride_item, amount)

        if amount <= ride_item.unpaid_price:
            ride_item.unpaid_price -= amount
            
        else:
           ride_item.unpaid_price -= amount
           print(f"you paid {amount} using Bank Transfer")
           print(f"you paid more than the total price, we returned {amount - ride_item.unpaid_price}")

        print(f"you paid {amount} using Bank Transfer")

        if ride_item.unpaid_price == 0:
            print("you paid all your debt")
            return True
            
        elif ride_item.unpaid_price > 0:
            print(f"you still have {ride_item.unpaid_price} tl to pay")
            return False
