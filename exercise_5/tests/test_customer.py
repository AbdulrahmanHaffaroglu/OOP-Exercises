import pytest

from e_commerce_order_system.models import Customer, Order


class TestCustomer:

	# -------------------------
	# Object creation
	# -------------------------

	def test_creation(self):
		# Arrange
		customer = Customer("Abdulrahman", 101, "abdulrahman@example.com")

		# Assert
		assert customer.name == "Abdulrahman"
		assert customer.customer_id == 101
		assert customer.email == "abdulrahman@example.com"
		assert customer.orders == []

	# -------------------------
	# Normal behavior
	# -------------------------

	def test_customer_can_have_multiple_orders(self):
		# Arrange
		customer = Customer("Abdulrahman", 101, "abdulrahman@example.com")

		# Act
		first_order = Order(1001, customer)
		second_order = Order(1002, customer)

		# Assert
		assert customer.orders == [first_order, second_order]

	# -------------------------
	# Invalid inputs
	# -------------------------

	def test_rejects_negative_id(self):
		with pytest.raises(ValueError):
			Customer("Abdulrahman", -1, "abdulrahman@example.com")
