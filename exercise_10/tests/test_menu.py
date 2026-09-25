import pytest

from restaurant_order_system.models.restaurant import Restaurant
from restaurant_order_system.models.the_menu.desserts import Dessert
from restaurant_order_system.models.customer import Customer


class TestMenu:
    def test_add_view_and_find_item(self):
        restaurant = Restaurant()
        cake = Dessert("Cake", "Chocolate cake", 120, True)

        restaurant.add_to_menu(cake)

        assert restaurant.view_menu() == [cake]
        assert restaurant.find_menu_item(cake.id) is cake

    def test_find_missing_item(self):
        restaurant = Restaurant()

        with pytest.raises(ValueError):
            restaurant.find_menu_item("missing")

    def test_remove_item(self):
        restaurant = Restaurant()
        cake = Dessert("Cake", "Chocolate cake", 120, True)
        restaurant.add_to_menu(cake)

        restaurant.remove_from_menu(cake)

        assert restaurant.view_menu() == []

    def test_incoming_orders_are_isolated_by_menu(self):
        first_restaurant = Restaurant()
        second_restaurant = Restaurant()
        first_item = Dessert("First", "", 10, True)
        second_item = Dessert("Second", "", 20, True)
        first_restaurant.add_to_menu(first_item)
        second_restaurant.add_to_menu(second_item)

        first_order = Customer("A", "a").create_order([first_item])
        second_order = Customer("B", "b").create_order([second_item])

        assert first_order in first_restaurant.incoming_orders()
        assert first_order not in second_restaurant.incoming_orders()
        assert second_order in second_restaurant.incoming_orders()
