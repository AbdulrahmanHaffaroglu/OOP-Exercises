import pytest

from e_commerce_order_system.models import Customer, Order, Product


@pytest.fixture
def customer():
	return Customer("Abdulrahman", 101, "abdulrahman@example.com")


@pytest.fixture
def products():
	return (
		Product(1, "Laptop", 1500, 10),
		Product(2, "Mouse", 50, 20),
		Product(3, "Keyboard", 100, 15),
	)


class TestOrder:

	# -------------------------
	# Object creation
	# -------------------------

	def test_creation(self, customer):
		# Arrange
		order = Order(1001, customer)

		# Assert
		assert order.status == "pending"
		assert order.order_items == ()
		assert order.customer is customer
		assert customer.orders == [order]

	# -------------------------
	# Normal behavior
	# -------------------------

	def test_add_remove_products_and_calculate_total(self, customer, products):
		# Arrange
		laptop, mouse, _ = products
		order = Order(1001, customer)

		# Act
		order.add_product(laptop, 2)
		order.add_product(mouse, 3)
		order.del_product(mouse)

		# Assert
		assert order.total_price() == 3000
		assert len(order.order_items) == 1
		assert order.order_items[0].product is laptop

	def test_three_orders_can_share_products_without_sharing_item_data(
		self, products
	):
		# Arrange
		laptop, mouse, keyboard = products
		first_customer = Customer("Abdulrahman", 101, "a@example.com")
		second_customer = Customer("Muhammad", 102, "m@example.com")
		first_order = Order(1001, first_customer)
		second_order = Order(1002, first_customer)
		third_order = Order(1003, second_customer)

		# Act
		first_order.add_product(laptop, 2)
		first_order.add_product(mouse, 3)
		second_order.add_product(keyboard, 2)
		third_order.add_product(mouse, 5)

		# Assert
		assert first_order.total_price() == 3150
		assert second_order.total_price() == 200
		assert third_order.total_price() == 250
		assert first_order.order_items[1] is not third_order.order_items[0]
		assert first_customer.orders == [first_order, second_order]
		assert second_customer.orders == [third_order]

	def test_paid_order_deducts_stock_and_cannot_be_changed(
		self, customer, products
	):
		# Arrange
		laptop, _, _ = products
		order = Order(1001, customer)
		order.add_product(laptop, 2)

		# Act
		order.change_status("paid")

		# Assert
		assert order.status == "paid"
		assert laptop.quantity == 8
		with pytest.raises(ValueError):
			order.order_items[0].quantity = 3
		with pytest.raises(ValueError):
			order.order_items[0].price = 1600
		with pytest.raises(ValueError):
			order.add_product(Product(4, "Camera", 500, 1), 1)
		with pytest.raises(ValueError):
			order.del_product(laptop)
		with pytest.raises(ValueError):
			order.change_status("pending")
		order.change_status("cancelled")
		assert laptop.quantity == 10

	def test_cancelling_paid_order_restores_stock(self, customer, products):
		# Arrange
		laptop, mouse, _ = products
		order = Order(1001, customer)
		order.add_product(laptop, 2)
		order.add_product(mouse, 3)
		order.change_status("paid")

		# Act
		order.change_status("cancelled")

		# Assert
		assert order.status == "cancelled"
		assert laptop.quantity == 10
		assert mouse.quantity == 20

	# -------------------------
	# Invalid inputs
	# -------------------------

	def test_rejects_negative_id(self, customer):
		with pytest.raises(ValueError):
			Order(-1, customer)

	def test_rejects_duplicate_missing_and_overstocked_products(
		self, customer, products
	):
		laptop, _, _ = products
		order = Order(1001, customer)
		order.add_product(laptop, 2)

		with pytest.raises(ValueError):
			order.add_product(laptop, 1)
		with pytest.raises(ValueError):
			order.add_product(Product(4, "Camera", 500, 1), 2)
		with pytest.raises(ValueError):
			order.del_product(Product(5, "Tablet", 300, 1))

	def test_payment_is_atomic_when_any_item_has_insufficient_stock(self, customer):
		available = Product(1, "Laptop", 1500, 10)
		unavailable = Product(2, "Mouse", 50, 2)
		order = Order(1001, customer)
		order.add_product(available, 2)
		order.add_product(unavailable, 2)
		unavailable.quantity = 1

		with pytest.raises(ValueError):
			order.change_status("paid")

		assert order.status == "pending"
		assert available.quantity == 10
		assert unavailable.quantity == 1

	def test_cancelled_order_cannot_be_paid_or_changed(self, customer, products):
		laptop, _, _ = products
		order = Order(1001, customer)
		order.add_product(laptop, 1)
		order.change_status("cancelled")

		with pytest.raises(ValueError):
			order.change_status("paid")
		with pytest.raises(ValueError):
			order.add_product(Product(4, "Camera", 500, 1), 1)
		with pytest.raises(ValueError):
			order.del_product(laptop)

	def test_shipped_order_cannot_be_cancelled_or_move_backwards(
		self, customer, products
	):
		laptop, _, _ = products
		order = Order(1001, customer)
		order.add_product(laptop, 1)
		order.change_status("shipped")

		with pytest.raises(ValueError):
			order.change_status("cancelled")
		with pytest.raises(ValueError):
			order.change_status("pending")
		with pytest.raises(ValueError):
			order.add_product(Product(4, "Camera", 500, 1), 1)

	def test_rejects_unknown_status(self, customer):
		order = Order(1001, customer)

		with pytest.raises(ValueError):
			order.change_status("delivered")
