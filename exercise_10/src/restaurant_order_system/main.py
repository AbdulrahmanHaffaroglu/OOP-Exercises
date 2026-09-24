from .models.customer import Customer
from .models.payment.credit_card import CreditCard
from .models.restaurant import Restaurant
from .models.the_menu.desserts import Dessert
from .models.the_menu.drinks import Drink
from .models.the_menu.main_dish import MainDish
from .models.the_menu.option import Option
from .utils.discounts import PercentageDiscount


def main():
        """Run a complete customer and staff workflow."""
        restaurant = Restaurant()

        cheese = Option("Extra cheese", 30)
        sauce = Option("Extra sauce", 15)
        large = Option("Large", 50)

        burger = MainDish("Chicken Burger", "Grilled chicken burger", 180, True, [cheese, sauce])
        cola = Drink("Cola", "Carbonated soft drink", 0, True, [large])
        cake = Dessert("Chocolate Cake", "Slice of chocolate cake", 120, True)

        for menu_item in (burger, cola, cake):
                restaurant.add_to_menu(menu_item)

        customer = Customer("Abdulrahman", "abdulrahman@example.com")
        order = customer.create_order([])
        customer.add_item(burger, order, quantity=2, options=[cheese, sauce])
        customer.add_item(cola, order, options=[large])
        customer.add_item(cake, order)

        print("Menu:", [item.name for item in restaurant.view_menu()])
        print("Subtotal:", order.total_price)

        customer.apply_discount(order, PercentageDiscount(10))
        customer.pay_order(order, CreditCard(customer))

        restaurant.confirm_order(order)
        restaurant.prepare_order(order)
        restaurant.ready_order(order)
        restaurant.deliver_order(order)

        print("Order summary:")
        print(order.summary())
        return order


if __name__ == "__main__":
        main()