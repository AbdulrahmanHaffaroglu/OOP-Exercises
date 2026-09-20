"""Run a small e-commerce order scenario."""

from e_commerce_order_system.models import Customer, Order, Product


def main():
    # Products
    laptop = Product(1, "Laptop", 1500, 10)
    mouse = Product(2, "Mouse", 50, 20)
    keyboard = Product(3, "Keyboard", 100, 15)

    # Customers
    abdulrahman = Customer(
        "Abdulrahman",
        101,
        "abdulrahman@example.com",
    )
    muhammad = Customer(
        "Muhammad",
        102,
        "muhammad@example.com",
    )

    # Orders
    order1 = Order(1001, abdulrahman)
    order2 = Order(1002, abdulrahman)
    order3 = Order(1003, muhammad)

    # Add and remove products
    order1.add_product(laptop, 2)
    order1.add_product(mouse, 3)

    order2.add_product(keyboard, 2)
    order2.del_product(keyboard)
    order2.add_product(keyboard, 1)

    order3.add_product(mouse, 5)

    # Calculate totals
    print("Order 1 total:", order1.total_price())
    print("Order 2 total:", order2.total_price())
    print("Order 3 total:", order3.total_price())

    # Demonstrate the price snapshot
    print("\nLaptop price before change:", laptop.price)
    laptop.price = 1700
    print("Laptop current price:", laptop.price)
    print("Order 1 laptop price:", order1.order_items[0].price)

    # Pay order 1
    print("\nPaying Order 1...")
    order1.change_status("paid")
    print("Order 1 status:", order1.status)
    print("Laptop stock:", laptop.quantity)
    print("Mouse stock:", mouse.quantity)

    # Cancel order 1 and restore its stock
    print("\nCancelling Order 1...")
    order1.change_status("cancelled")
    print("Order 1 status:", order1.status)
    print("Laptop stock:", laptop.quantity)
    print("Mouse stock:", mouse.quantity)

    # One customer can have multiple orders.
    print("\nAbdulrahman's orders:", len(abdulrahman.orders))


if __name__ == "__main__":
    main()
