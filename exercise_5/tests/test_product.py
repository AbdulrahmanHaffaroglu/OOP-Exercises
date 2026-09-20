import pytest

from e_commerce_order_system.models import Product


class TestProduct:

	# -------------------------
	# Object creation
	# -------------------------

	def test_creation(self):
		# Arrange
		product = Product(1, "Laptop", 1500, 10)

		# Assert
		assert product.product_id == 1
		assert product.name == "Laptop"
		assert product.price == 1500
		assert product.quantity == 10

	# -------------------------
	# Normal behavior
	# -------------------------

	def test_stock_can_increase_and_decrease(self):
		# Arrange
		product = Product(1, "Laptop", 1500, 10)

		# Act
		product.increase_stock(5)
		product.decrease_stock(3)

		# Assert
		assert product.quantity == 12

	# -------------------------
	# Properties / getters
	# -------------------------

	def test_price_and_quantity_properties(self):
		product = Product(1, "Laptop", 1500, 10)

		assert product.price == 1500
		assert product.quantity == 10

	# -------------------------
	# Setters / modification
	# -------------------------

	def test_price_and_quantity_setters(self):
		product = Product(1, "Laptop", 1500, 10)

		product.price = 1700
		product.quantity = 12

		assert product.price == 1700
		assert product.quantity == 12

	# -------------------------
	# Invalid inputs
	# -------------------------

	@pytest.mark.parametrize(
		"factory",
		[
			lambda: Product(-1, "Laptop", 1500, 10),
			lambda: Product(1, "Laptop", -1, 10),
			lambda: Product(1, "Laptop", 1500, -1),
		],
	)
	def test_rejects_negative_values(self, factory):
		with pytest.raises(ValueError):
			factory()

	@pytest.mark.parametrize(
		"operation",
		[
			lambda product: product.price_setter(-1),
			lambda product: product.quantity_setter(-1),
			lambda product: product.increase_stock(-1),
			lambda product: product.decrease_stock(-1),
			lambda product: product.decrease_stock(11),
		],
	)
	def test_rejects_invalid_stock_and_price_operations(self, operation):
		product = Product(1, "Laptop", 1500, 10)

		with pytest.raises(ValueError):
			operation(product)

		assert product.quantity == 10
		assert product.price == 1500
