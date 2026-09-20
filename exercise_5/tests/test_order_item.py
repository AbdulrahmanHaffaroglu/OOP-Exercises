import pytest

from e_commerce_order_system.models import OrderItem, Product


class TestOrderItem:

	# -------------------------
	# Object creation
	# -------------------------

	def test_creation(self):
		product = Product(1, "Laptop", 1500, 10)
		item = OrderItem(product, 2)

		assert item.product is product
		assert item.quantity == 2
		assert item.price == 1500

	# -------------------------
	# Normal behavior
	# -------------------------

	def test_price_is_snapshot_when_product_price_changes(self):
		# Arrange
		product = Product(1, "Laptop", 1500, 10)
		item = OrderItem(product, 2)

		# Act
		product.price = 1700

		# Assert
		assert item.price == 1500

	# -------------------------
	# Properties / getters
	# -------------------------

	def test_properties_return_item_data(self):
		product = Product(1, "Laptop", 1500, 10)
		item = OrderItem(product, 2)

		assert item.product is product
		assert item.quantity == 2
		assert item.price == 1500

	# -------------------------
	# Setters / modification
	# -------------------------

	def test_properties_can_be_updated_with_valid_values(self):
		product = Product(1, "Laptop", 1500, 10)
		item = OrderItem(product, 2)

		item.price = 1600
		item.quantity = 3

		assert item.price == 1600
		assert item.quantity == 3

	# -------------------------
	# Invalid inputs
	# -------------------------

	@pytest.mark.parametrize("quantity", [0, -1, 11])
	def test_rejects_invalid_quantity_or_insufficient_stock(self, quantity):
		product = Product(1, "Laptop", 1500, 10)

		with pytest.raises(ValueError):
			OrderItem(product, quantity)

	@pytest.mark.parametrize("attribute", ["price", "quantity"])
	def test_properties_reject_invalid_values(self, attribute):
		product = Product(1, "Laptop", 1500, 10)
		item = OrderItem(product, 2)

		with pytest.raises(ValueError):
			setattr(item, attribute, -1 if attribute == "price" else 0)
