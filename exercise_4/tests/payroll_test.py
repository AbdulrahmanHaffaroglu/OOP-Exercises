from employee_payrol_system.models.contractor import Contractor
from employee_payrol_system.services.payroll import payroll_function


class TestPayroll:

	# -------------------------
	# Normal behavior
	# -------------------------

	def test_payroll_function_prints_salary_and_bonus(self, capsys):
		employee = Contractor('Abdulrahman', 11001, 50000)

		payroll_function(employee)

		captured = capsys.readouterr()
		assert captured.out == (
			'employee Abdulrahman salary is 50000\n'
			'employee Abdulrahman bonus is 2500.0\n'
			'\n'
		)
