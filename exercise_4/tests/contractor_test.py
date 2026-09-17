import pytest

# Import the class being tested
from employee_payrol_system.models.contractor import Contractor


class TestContractor:

	# -------------------------
	# Object creation
	# -------------------------

	def test_creation(self):
		employee = Contractor('Abdulrahman', 11001, 50000)

		assert employee.name == 'Abdulrahman'
		assert employee.emp_id == 11001

	# -------------------------
	# Normal behavior
	# -------------------------

	def test_clc_salary_method(self):
		employee = Contractor('Abdulrahman', 11001, 50000)

		assert employee.clc_salary() == 50000

	def test_clc_bonus_method(self):
		employee = Contractor('Abdulrahman', 11001, 50000)

		assert employee.clc_bonus() == 2500

	# -------------------------
	# Properties / getters
	# -------------------------

	def test_prjt_pay_getter(self):
		employee = Contractor('Abdulrahman', 11001, 50000)

		assert employee.prjt_pay == 50000

	# -------------------------
	# Setters / modification
	# -------------------------

	def test_prjt_pay_setter(self):
		employee = Contractor('Abdulrahman', 11001, 50000)

		employee.prjt_pay = 60000

		assert employee.prjt_pay == 60000

	# -------------------------
	# Invalid inputs
	# -------------------------

	def test_invalid_id(self):
		with pytest.raises(ValueError):
			Contractor('Abdulrahman', -11001, 50000)

	def test_invalid_payment(self):
		with pytest.raises(ValueError):
			Contractor('Abdulrahman', 11001, -50000)

	def test_invalid_payment_setter(self):
		employee = Contractor('Abdulrahman', 11001, 50000)

		with pytest.raises(ValueError):
			employee.prjt_pay = -60000

	# -------------------------
	# Edge cases
	# -------------------------

	def test_zero_payment(self):
		employee = Contractor('Abdulrahman', 11001, 0)

		assert employee.clc_salary() == 0
		assert employee.clc_bonus() == 0
