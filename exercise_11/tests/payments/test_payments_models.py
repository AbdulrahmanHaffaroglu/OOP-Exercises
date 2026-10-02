from types import SimpleNamespace

import pytest

from mini_uber_system.models.Payment_Methods.bank_transfer import BankTransfer
from mini_uber_system.models.Payment_Methods.cash import Cash
from mini_uber_system.models.Payment_Methods.credit_card import CreditCard
from mini_uber_system.models.Payment_Methods.payment import Payment


PAYMENT_TYPES = [Cash, BankTransfer, CreditCard]


class TestPaymentMethods:
	# Object creation
	@pytest.mark.parametrize('payment_type', PAYMENT_TYPES)
	def test_payment_method_creation(self, payment_type):
		assert isinstance(payment_type(), Payment)

	# Normal behavior
	@pytest.mark.parametrize('payment_type', PAYMENT_TYPES)
	def test_partial_payment_reduces_unpaid_balance(self, payment_type, capsys):
		ride = SimpleNamespace(unpaid_price=200)

		result = payment_type().pay(ride, 75)

		assert result is False
		assert ride.unpaid_price == 125
		assert 'still have 125' in capsys.readouterr().out

	@pytest.mark.parametrize('payment_type', PAYMENT_TYPES)
	def test_exact_payment_clears_balance(self, payment_type, capsys):
		ride = SimpleNamespace(unpaid_price=200)

		result = payment_type().pay(ride, 200)

		assert result is True
		assert ride.unpaid_price == 0
		assert 'paid all your debt' in capsys.readouterr().out

	# Invalid inputs
	@pytest.mark.parametrize('payment_type', PAYMENT_TYPES)
	@pytest.mark.parametrize('amount', [0, -1])
	def test_nonpositive_payment_is_rejected(self, payment_type, amount):
		ride = SimpleNamespace(unpaid_price=200)

		with pytest.raises(ValueError):
			payment_type().pay(ride, amount)

	def test_payment_base_class_is_abstract(self):
		with pytest.raises(TypeError):
			Payment()

	# Edge cases
	@pytest.mark.parametrize('payment_type', PAYMENT_TYPES)
	def test_overpayment_does_not_create_negative_balance(self, payment_type, capsys):
		ride = SimpleNamespace(unpaid_price=200)

		result = payment_type().pay(ride, 250)

		assert result is True
		assert ride.unpaid_price == 0
