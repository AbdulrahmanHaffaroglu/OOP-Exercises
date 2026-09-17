import pytest

# Import the class/function being tested
from employee_payrol_system.models.part_time_employee import Part_time


class TestPartTimeEmployee:

    # -------------------------
    # Object creation
    # -------------------------

    def test_creation(self):
        # Arrange
        employee = Part_time('Abdulrahman', 283912, 18, 200)

        # Assert
        assert employee.name == 'Abdulrahman'
        assert employee.emp_id == 283912


    # -------------------------
    # Normal behavior
    # -------------------------

    def test_clc_salary_method(self):
        # Arrange
        employee = Part_time('Abdulrahman', 283912, 18, 200)

        # Act
        result = employee.clc_salary()

        # Assert
        assert result == 18 * 200

    def test_clc_bonus_method(self):
        # Arrange
        employee = Part_time('Abdulrahman', 283912, 18, 200)

        # Act
        result = employee.clc_bonus()

        # Assert
        assert result == 0

    # -------------------------
    # Properties / getters
    # -------------------------

    def test_hr_rate_getter(self):
        employee = Part_time('Abdulrahman', 283912, 18, 200)

        assert employee.hr_rate == 18


    def test_work_hrs_getter(self):
        employee = Part_time('Abdulrahman', 283912, 18, 200)

        assert employee.work_hrs == 200


    # -------------------------
    # Setters / modification
    # -------------------------

    def test_hr_rate_setter(self):
        employee = Part_time('Abdulrahman', 283912, 18, 200)

        employee.hr_rate = 20

        assert employee.hr_rate == 20

    def test_work_hrs_setter(self):
        employee = Part_time('Abdulrahman', 283912, 18, 200)

        employee.work_hrs = 225

        assert employee.work_hrs == 225


    # -------------------------
    # Invalid inputs
    # -------------------------

    def test_invalid_id(self):
        with pytest.raises(ValueError):
            Part_time('Abdulrahman', -283912, 18, 200)

    def test_invalid_hr_rate(self):
        with pytest.raises(ValueError):
            Part_time('Abdulrahman', 283912, -18, 200)

    def test_invalid_work_hrs(self):
        with pytest.raises(ValueError):
            Part_time('Abdulrahman', 283912, 18, -200)

    # -------------------------
    # Edge cases
    # -------------------------

    def test_setting_negative_hr_rate_case(self):
        employee = Part_time('Abdulrahman', 283912, 18, 200)

        with pytest.raises(ValueError):
            employee.hr_rate = -124

    def test_setting_negative_work_hrs_case(self):
        employee = Part_time('Abdulrahman', 283912, 18, 200)

        with pytest.raises(ValueError):
            employee.work_hrs = -240