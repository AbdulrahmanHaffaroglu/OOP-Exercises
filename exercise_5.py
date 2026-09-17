'''
Build an e-commerce order system.

# Requirements
The system must support:

Products
Customers
Orders
Order items



Every product has:

Product ID
Name
Price
Stock quantity

A product must:

Allow its stock to increase.
Allow its stock to decrease.
Reject invalid prices.
Reject invalid stock quantities.
Never allow stock to become negative.



Every customer has:

Customer ID
Name
Email

- A customer can have multiple orders.



Every order has:

Order ID
Customer
A collection of order items
An order status

Supported statuses:

Pending
Paid
Shipped
Cancelled

An order must be able to:

Add a product with a quantity.
Remove a product.
Calculate its total price.
Change its status.


An order item represents:

A product
Quantity
Price at the time it was added

The item's price should not change if the product's price changes later.

Example:

Product price when ordered: $100
Order item price: $100

Product price later changes to: $120

Existing order item: still $100

Business rules
An order cannot contain zero or negative quantities.
An order cannot add more items than the product's available stock.
Cancelled orders cannot be paid.
Shipped orders cannot be cancelled.
A paid order cannot have products added or removed.
When an order is successfully paid, the required stock should be deducted.
If an order is cancelled after payment, the stock should be restored.
The same product should not appear as multiple separate items in one order.
System requirements
A customer can have multiple orders.
A product can appear in many different orders.
Different orders must maintain their own item data.
Product price changes must not modify existing orders.
Invalid operations should be rejected without corrupting the order.


#OOP requirements

Your implementation must demonstrate:

Encapsulation
Composition
Association
Properties
Object interaction
State management
Appropriate separation of responsibilities
Testing requirements

Create:

At least 3 products
At least 2 customers
At least 3 orders

Demonstrate:

Adding/removing products from orders
Calculating order totals
Changing product prices after an order is created
Paying an order
Cancelling an order
Restoring stock after cancellation
At least 5 invalid operations
'''

class Product:
    def __init__(self, product_id, name, price, quantity):
        if price < 0:
            raise ValueError("price can't be negative")

        if quantity < 0:
            raise ValueError("quantity can't be negative")

        if product_id < 0:
            raise ValueError("product id can't be negative")

        self.product_id = product_id
        self.name = name
        self._price = price
        self._quantity = quantity

    # Getter functions
    def quantity_getter(self):
        return self._quantity

    def price_getter(self):
        return self._price

    # Setter functions
    def quantity_setter(self, quantity):
        if quantity < 0:
            raise ValueError("quantity can't be negative")

        self._quantity = quantity

    def price_setter(self, price):
        if price < 0:
            raise ValueError("price can't be negative")

        self._price = price

    # Stock functions
    def increase_stock(self, amount):
        if amount < 0:
            raise ValueError(
                "you can't increase the stock with a negative amount"
            )

        self._quantity += amount

    def decrease_stock(self, amount):
        if amount < 0:
            raise ValueError(
                "you can't decrease the stock with a negative amount"
            )

        if self._quantity < amount:
            raise ValueError("stock quantity shouldn't become negative")

        self._quantity -= amount

    quantity = property(
        fget=quantity_getter,
        fset=quantity_setter
    )

    price = property(
        fget=price_getter,
        fset=price_setter
    )


# Customer class
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


# Order class
class Order:

    valid_status = [
        "pending",
        "paid",
        "shipped",
        "cancelled"
    ]

    def __init__(self, order_id, customer):

        if order_id < 0:
            raise ValueError("order id can't be negative")

        self.order_id = order_id
        self._order_items = []
        self._status = "pending"
        self.customer = customer

        customer._orders.append(self)

    @property
    def status(self):
        return self._status

    @property
    def order_items(self):
        return self._order_items

    def add_product(self, product, quantity):

        if self._status == "paid":
            raise ValueError("paid orders cannot be changed")

        if self._status in ["shipped", "cancelled"]:
            raise ValueError(
                "shipped or cancelled orders cannot be changed"
            )

        # Prevent the same product from appearing twice
        for item in self._order_items:
            if item.product is product:
                raise ValueError(
                    "the product already exists in this order"
                )

        item = self.OrderItem(product, quantity)
        self._order_items.append(item)

    def del_product(self, product):

        if self._status == "paid":
            raise ValueError("paid orders cannot be changed")

        if self._status in ["shipped", "cancelled"]:
            raise ValueError(
                "shipped or cancelled orders cannot be changed"
            )

        for item in self._order_items:
            if item.product is product:
                self._order_items.remove(item)
                return

        raise ValueError("product is not in this order")

    def total_price(self):
        return sum(
            item.price * item.quantity
            for item in self._order_items
        )

    def change_status(self, status):

        if status not in self.valid_status:
            raise ValueError("this is not a valid status")

        # Same status
        if self._status == status:
            return

        # Shipped orders cannot be cancelled
        if self._status == "shipped" and status == "cancelled":
            raise ValueError("shipped orders cannot be cancelled")

        # Cancelled orders cannot be paid
        if self._status == "cancelled" and status == "paid":
            raise ValueError("cancelled orders cannot be paid")

        # Paid orders cannot go back to pending
        if self._status == "paid" and status == "pending":
            raise ValueError("paid orders cannot return to pending")

        # Shipped orders cannot go backwards
        if self._status == "shipped":
            raise ValueError("shipped orders cannot change status")

        # Pay the order
        if status == "paid":

            # First verify ALL products have enough stock.
            # This prevents partially changing the stock.
            for item in self._order_items:
                if item.product.quantity < item.quantity:
                    raise ValueError(
                        f"not enough stock for {item.product.name}"
                    )

            # Only modify stock after all checks succeed.
            for item in self._order_items:
                item.product.decrease_stock(item.quantity)

        # Cancel a paid order and restore its stock
        if self._status == "paid" and status == "cancelled":

            for item in self._order_items:
                item.product.increase_stock(item.quantity)

        self._status = status

    # OrderItem class
    class OrderItem:

        def __init__(self, product, quantity):

            if quantity <= 0:
                raise ValueError(
                    "ordered item's quantity must be greater than zero"
                )

            if product.quantity < quantity:
                raise ValueError(
                    f"not enough stock for {product.name}"
                )

            self.product = product

            # Price snapshot
            self._price = product.price

            # Quantity ordered
            self._quantity = quantity

        # Price setter
        def price_setter(self, price):
            if price < 0:
                raise ValueError("price can't be negative")

            self._price = price

        # Quantity setter
        def quantity_setter(self, quantity):
            if quantity <= 0:
                raise ValueError(
                    "ordered item's quantity must be greater than zero"
                )

            self._quantity = quantity

        # Getters
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


# -------------------------
# Testing
# -------------------------

if __name__ == "__main__":

    # Products
    laptop = Product(
        1,
        "Laptop",
        1500,
        10
    )

    mouse = Product(
        2,
        "Mouse",
        50,
        20
    )

    keyboard = Product(
        3,
        "Keyboard",
        100,
        15
    )

    # Customers
    abdulrahman = Customer(
        "Abdulrahman",
        101,
        "abdulrahman@example.com"
    )

    muhammad = Customer(
        "Muhammad",
        102,
        "muhammad@example.com"
    )

    # Orders
    order1 = Order(1001, abdulrahman)
    order2 = Order(1002, abdulrahman)
    order3 = Order(1003, muhammad)

    # Add products
    order1.add_product(laptop, 2)
    order1.add_product(mouse, 3)

    order2.add_product(keyboard, 2)

    order3.add_product(mouse, 5)

    # Calculate totals
    print("Order 1 total:", order1.total_price())
    print("Order 2 total:", order2.total_price())
    print("Order 3 total:", order3.total_price())

    # Demonstrate price snapshot
    print("\nLaptop price before change:", laptop.price)

    laptop.price = 1700

    print("Laptop current price:", laptop.price)
    print(
        "Order 1 laptop price:",
        order1.order_items[0].price
    )

    # Pay order 1
    print("\nPaying Order 1...")
    order1.change_status("paid")

    print("Order 1 status:", order1.status)
    print("Laptop stock:", laptop.quantity)
    print("Mouse stock:", mouse.quantity)

    # Cancel order 1
    print("\nCancelling Order 1...")
    order1.change_status("cancelled")

    print("Order 1 status:", order1.status)
    print("Laptop stock:", laptop.quantity)
    print("Mouse stock:", mouse.quantity)

    # Customer orders
    print(
        "\nAbdulrahman's orders:",
        len(abdulrahman.orders)
    )

    # -------------------------
    # Invalid operations
    # -------------------------

    print("\nInvalid operations:")

    # 1. Negative product price
    try:
        Product(4, "Bad Product", -100, 10)
    except ValueError as e:
        print("1.", e)

    # 2. Negative stock
    try:
        Product(5, "Bad Product", 100, -10)
    except ValueError as e:
        print("2.", e)

    # 3. Add negative quantity
    try:
        order2.add_product(mouse, -2)
    except ValueError as e:
        print("3.", e)

    # 4. Add same product twice
    try:
        order2.add_product(keyboard, 1)
    except ValueError as e:
        print("4.", e)

    # 5. Pay cancelled order
    try:
        order1.change_status("paid")
    except ValueError as e:
        print("5.", e)

    # 6. Cancel shipped order
    try:
        order3.change_status("paid")
        order3.change_status("shipped")
        order3.change_status("cancelled")
    except ValueError as e:
        print("6.", e)

    # 7. Add product to paid order
    try:
        order3.add_product(laptop, 1)
    except ValueError as e:
        print("7.", e)