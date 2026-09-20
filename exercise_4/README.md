# Employee Payroll System

A small Python object-oriented payroll system demonstrating inheritance, abstract base classes, properties, validation, and pytest testing.

## Features

- Abstract `Employee` base class with shared name and employee ID fields.
- Full-time employees with a monthly base salary and a 10% bonus.
- Part-time employees with an hourly rate and worked hours. Their salary is calculated as `hourly rate * worked hours` and their bonus is `0`.
- Contractors with project payment and a 5% bonus.
- Validation that prevents negative IDs, salaries, payments, hourly rates, and working hours.
- Payroll service that prints an employee's salary and bonus.

## Project Structure

```text
src/employee_payrol_system/
├── models/
│   ├── employees.py
│   ├── full_time_employee.py
│   ├── part_time_employee.py
│   └── contractor.py
└── services/
	└── payroll.py
tests/
├── employee_test.py
├── full_time_employee_test.py
├── part_time_employee_test.py
├── contractor_test.py
└── payroll_test.py
```

## Requirements

- Python 3.9 or newer
- pytest

## Installation

Open the `exercise_4` folder itself as the VS Code workspace. It is the
project root and contains `pyproject.toml`, `src/`, and `tests/`.

Create and activate a virtual environment, then install the project and test dependency:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the project and its test dependency:

```bash
python -m pip install -e ".[test]"
```

## Usage

```python
from employee_payrol_system.models.full_time_employee import Full_time
from employee_payrol_system.models.part_time_employee import Part_time
from employee_payrol_system.models.contractor import Contractor
from employee_payrol_system.services.payroll import payroll_function

full_time = Full_time("Abdulrahman", 11001, 35000)
part_time = Part_time("Sara", 11002, 18, 200)
contractor = Contractor("Omar", 11003, 50000)

print(full_time.mth_base_slr)  # 35000
part_time.work_hrs = 220
contractor.prjt_pay = 55000

payroll_function(full_time)
payroll_function(part_time)
payroll_function(contractor)
```

The payroll service prints output in this format:

```text
employee Abdulrahman salary is 35000
employee Abdulrahman bonus is 3500.0
```

## Running Tests

Run the complete test suite from the project root:

```bash
python -m pytest -q
```

The tests cover employee creation, salary and bonus calculations, properties, setters, validation, edge cases, and payroll output.
