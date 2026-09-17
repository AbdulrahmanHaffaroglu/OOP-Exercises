'''  
Create a BankAccount class with:
- owner
- balance
- account_number


Methods:
- deposit(amount)
- withdraw(amount)
- get_balance()


Rules:
- You can't deposit a negative amount.
- You can't withdraw more than the balance.
- The balance shouldn't be directly modifiable from outside the class.

Tests: classes, constructors, methods, encapsulation.   '''


class BankAccount:

    def __init__(self, owner, account_number):
        self._balance = 0
        self.owner = owner
        self.account_number = account_number

    def deposit(self,amount):
        if amount < 0:
            print("You can't deposit a negative amount")
        else:
            self._balance += amount
            print(f"{amount}$ was added to your account balance")

    def withdraw(self, amount):
        if amount > self._balance:
            print("You can't withdraw more than the balance")
        elif amount < 0:
            print("You can't withdraw a negative amount")
        else:
            self._balance -= amount
            print(f"{amount}$ was withdrawen from your account balance")

    def get_balance(self):
        return self._balance


if __name__ == "__main__":
    b1 = BankAccount("Abdulrahman", 1)
    b2 = BankAccount("Raphael", 2)


    b1.deposit(-10)
    b1.deposit(100)
    b2.deposit(-10)
    b2.deposit(200)


    b1.withdraw(1000)
    b1.withdraw(10)
    b2.withdraw(1000)
    b2.withdraw(20)

    print(b1.get_balance())
    print(b2.get_balance())


