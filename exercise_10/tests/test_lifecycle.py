import pytest

from restaurant_order_system.models.customer import Customer
from restaurant_order_system.models.restaurant import Restaurant
from restaurant_order_system.models.the_menu.desserts import Dessert


class TestOrderLifecycle:
    def test_status_lifecycle_requires_payment(self):
        customer = Customer("A", "contact")
        restaurant = Restaurant()
        order = customer.create_order([Dessert("Cake", "", 120, True)])

        with pytest.raises(ValueError):
            restaurant.confirm_order(order)

        customer.pay_order(order, __import__(
            "restaurant_order_system.models.payment.cash",
            fromlist=["Cash"],
        ).Cash(customer))
        restaurant.confirm_order(order)
        restaurant.prepare_order(order)
        restaurant.ready_order(order)
        restaurant.deliver_order(order)

        assert order.status == "Delivered"

    def test_cancel_pending_or_confirmed_but_not_preparing(self):
        customer = Customer("A", "contact")
        restaurant = Restaurant()
        pending = customer.create_order([Dessert("Cake", "", 120, True)])
        customer.cancel_order(pending)
        assert pending.status == "Cancelled"

        confirmed = customer.create_order([Dessert("Cake", "", 120, True)])
        confirmed.is_paid = True
        restaurant.confirm_order(confirmed)
        customer.cancel_order(confirmed)
        assert confirmed.status == "Cancelled"

        preparing = customer.create_order([Dessert("Cake", "", 120, True)])
        preparing.is_paid = True
        restaurant.confirm_order(preparing)
        restaurant.prepare_order(preparing)
        with pytest.raises(ValueError):
            customer.cancel_order(preparing)

    def test_order_history_and_summary(self):
        customer = Customer("A", "contact")
        order = customer.create_order([Dessert("Cake", "", 120, True)])

        history = customer.view_orders()

        assert history[0]["id"] == order.id
        assert history[0]["subtotal"] == 120
        assert history[0]["order_status"] == "Pending"
