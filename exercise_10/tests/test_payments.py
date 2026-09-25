import pytest

from restaurant_order_system.models.customer import Customer
from restaurant_order_system.models.payment.cash import Cash
from restaurant_order_system.models.the_menu.desserts import Dessert
from restaurant_order_system.utils.discounts import FixedDiscount


class TestPayments:
    def test_failed_payment_leaves_order_unpaid(self):
        customer = Customer("A", "contact")
        order = customer.create_order([Dessert("Cake", "", 120, True)])

        result = customer.pay_order(order, Cash(customer), succeeds=False)

        assert result is False
        assert order.is_paid is False
        assert order.status == "Pending"

    def test_payment_uses_discounted_total_and_cannot_repeat(self):
        customer = Customer("A", "contact")
        order = customer.create_order([Dessert("Cake", "", 120, True)])
        customer.apply_discount(order, FixedDiscount(20))

        customer.pay_order(order, Cash(customer))

        assert order.is_paid
        assert order.paid_total == 100
        assert order.final_total == 100
        with pytest.raises(ValueError):
            customer.pay_order(order, customer.cash_method)

    def test_empty_and_cancelled_orders_cannot_be_paid(self):
        customer = Customer("A", "contact")
        empty_order = customer.create_order([])
        with pytest.raises(ValueError):
            customer.pay_order(empty_order, Cash(customer))

        cancelled_order = customer.create_order([Dessert("Cake", "", 120, True)])
        customer.cancel_order(cancelled_order)
        with pytest.raises(ValueError):
            customer.pay_order(cancelled_order, customer.cash_method)

    def test_unregistered_payment_method_and_none_are_rejected(self):
        customer = Customer("A", "contact")
        other_customer = Customer("B", "contact")
        order = customer.create_order([Dessert("Cake", "", 120, True)])
        other_payment = Cash(other_customer)

        with pytest.raises(ValueError):
            customer.pay_order(order, other_payment)
        with pytest.raises(ValueError):
            customer.pay_order(order, None)

    def test_payment_freezes_final_total(self):
        customer = Customer("A", "contact")
        order = customer.create_order([Dessert("Cake", "", 120, True)])
        customer.pay_order(order, Cash(customer))

        with pytest.raises(ValueError):
            customer.apply_discount(order, FixedDiscount(20))
        assert order.final_total == 120
