import pytest

# Import the class/function being tested
from employee_payrol_system.models.employees import Employee


class TestEmployee:

    # -------------------------
    # Object creation
    # -------------------------

    def test_cannot_create_abstract_employee(self):
        with pytest.raises(TypeError):
            Employee('Abdulrahman', 11001)


    # -------------------------
    # Normal behavior
    # -------------------------


    # -------------------------
    # Invalid input
    # -------------------------

    def test_invalid_input(self):
        with pytest.raises(TypeError):
            employee = Employee('Abdulrahman', -12002)