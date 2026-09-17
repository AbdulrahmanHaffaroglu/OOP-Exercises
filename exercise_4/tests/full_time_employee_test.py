import pytest

# Import the class/function being tested
from employee_payrol_system.models.full_time_employee import Full_time


class Test_Full_time:

    # -------------------------
    # Object creation
    # -------------------------

    def test_creation(self):
        # Arrange
        employee = Full_time('Abdulrahman', 11001, 35000)

        # Assert
        assert employee.name == 'Abdulrahman'
        assert employee.emp_id == 11001


    # -------------------------
    # Normal behavior
    # -------------------------


    def test_clc_salary_method(self):
        # Arrange
        employee = Full_time('Abdulrahman', 11001, 35000)

        # Act
        result = employee.clc_salary()

        # Assert
        assert result == 35000

    def test_clc_bonus_method(self):
        # Arrange
        employee = Full_time('Abdulrahman', 11001, 35000)

        # Act
        result = employee.clc_bonus()

        # Assert
        assert result == 3500

    # -------------------------
    # Properties / getters
    # -------------------------

    def test_mth_base_slr_getter(self):
        employee = Full_time('Abdulrahman', 11001, 35000)

        assert employee.slr_getter() == 35000


    # -------------------------
    # Setters / modification
    # -------------------------

    def test_mth_base_slr_setter(self):
        employee = Full_time('Abdulrahman', 11001, 35000)

        employee.mth_base_slr = 12500

        assert employee.mth_base_slr == 12500
    # -------------------------
    # Invalid inputs
    # -------------------------

    def test_invalid_id(self):
        with pytest.raises(ValueError):
            employee = Full_time('Abdulrahman', -31131, 35000)

    def test_invalid_salary(self):
        with pytest.raises(ValueError):
            employee = Full_time('Abdulrahman', 11001, -12344)

        
    # -------------------------
    # Edge cases
    # -------------------------

    def test_edge_case_for_setter(self):
        employee = Full_time('Abdulrahman', 11001, 35000)

        with pytest.raises(ValueError):
            employee.mth_base_slr = -4256