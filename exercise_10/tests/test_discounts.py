import pytest

from restaurant_order_system.models.customer import Customer
from restaurant_order_system.models.the_menu.desserts import Dessert
from restaurant_order_system.utils.discounts import FixedDiscount, PercentageDiscount


class TestDiscounts:
    def test_percentage_discount(self):
        customer = Customer("A", "contact")
        order = customer.create_order([Dessert("Cake", "", 500, True)])

        result = customer.apply_discount(order, PercentageDiscount(10))

        assert result == 450
        assert order.discount_amount == 50
        assert order.final_total == 450

    def test_fixed_discount_cannot_make_total_negative(self):
        customer = Customer("A", "contact")
        order = customer.create_order([Dessert("Cake", "", 20, True)])

        assert customer.apply_discount(order, FixedDiscount(100)) == 0

    def test_discount_recalculates_after_order_changes(self):
        customer = Customer("A", "contact")
        cake = Dessert("Cake", "", 100, True)
        order = customer.create_order([cake])
        customer.apply_discount(order, PercentageDiscount(10))

        order.add_item(cake)

        assert order.total_price == 200
        assert order.discount_amount == 20
        assert order.final_total == 180

    def test_invalid_discounts(self):
        with pytest.raises(ValueError):
            PercentageDiscount(0)
        with pytest.raises(ValueError):
            PercentageDiscount(101)
        with pytest.raises(ValueError):
            FixedDiscount(0)
