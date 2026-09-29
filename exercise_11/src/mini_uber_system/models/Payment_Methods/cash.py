from .payment import Payment

class Cash(Payment):
    def pay(self, ride_item, amount):
        super().__init__(ride_item, amount)

        if amount <= ride_item.unpaid_price:
            ride_item.unpaid_price -= amount
            
        else:
           ride_item.unpaid_price -= amount
           print("you paid using Cash")
           print(f"you paid more than the total price, we returned {amount - ride_item.unpaid_price}")

        print("you paid using Cash")

        if ride_item.unpaid_price == 0:
            print("you paid all your debt")
            return True
            
        elif ride_item.unpaid_price > 0:
            print(f"you still have {ride_item.unpaid_price} tl to pay")
            return False
