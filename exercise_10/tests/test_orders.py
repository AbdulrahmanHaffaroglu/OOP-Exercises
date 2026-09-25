import pytest

from restaurant_order_system.models.customer import Customer
from restaurant_order_system.models.the_menu.desserts import Dessert
from restaurant_order_system.models.the_menu.drinks import Drink
from restaurant_order_system.models.the_menu.main_dish import MainDish
from restaurant_order_system.models.the_menu.option import Option


class TestOrders:
    def test_order_prices_include_options(self):
        customer = Customer("Abdulrahman", "contact")
        cheese = Option("Cheese", 30)
        burger = MainDish("Burger", "", 180, True, [cheese])
        cola = Drink("Cola", "", True, [Option("Large", 50)])
        cake = Dessert("Cake", "", 120, True)
        order = customer.create_order([])

        customer.add_item(burger, order, 2, [cheese])
        customer.add_item(cola, order, options=[cola.sizes.options[0]])
        customer.add_item(cake, order)

        assert order.total_price == 590

    def test_drink_requires_size_and_dessert_rejects_options(self):
        customer = Customer("A", "contact")
        drink = Drink("Cola", "", True, [Option("Small", 30)])
        cake = Dessert("Cake", "", 120, True)
        order = customer.create_order([])

        with pytest.raises(ValueError):
            customer.add_item(drink, order)
        with pytest.raises(ValueError):
            customer.add_item(cake, order, options=[Option("Cream", 10)])

    def test_invalid_quantity_and_unavailable_item(self):
        customer = Customer("A", "contact")
        cake = Dessert("Cake", "", 120, True)
        unavailable = Dessert("Unavailable", "", 50, False)
        order = customer.create_order([])

        with pytest.raises(ValueError):
            customer.add_item(cake, order, quantity=0)
        with pytest.raises(ValueError):
            customer.add_item(unavailable, order)

    def test_quantity_changes_and_removal(self):
        customer = Customer("A", "contact")
        cake = Dessert("Cake", "", 120, True)
        order = customer.create_order([cake])

        customer.increase_quantity(order, cake, 2)
        customer.reduce_quantity(order, cake, 1)
        assert order.total_price == 240

        customer.remove_item(cake, order)
        assert order.total_price == 0

    def test_paid_order_cannot_change(self):
        customer = Customer("A", "contact")
        cake = Dessert("Cake", "", 120, True)
        order = customer.create_order([cake])
        order.is_paid = True

        with pytest.raises(ValueError):
            order.add_item(cake)
        with pytest.raises(ValueError):
            order.remove_item(cake)
