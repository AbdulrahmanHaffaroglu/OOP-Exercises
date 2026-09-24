import pytest

from restaurant_order_system.models.restaurant import Restaurant
from restaurant_order_system.models.the_menu.desserts import Dessert


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
