'''
Build an employee payroll system.

Requirements
The system must support three types of employees:

Full-time employees
Part-time employees
Contractors

Every employee must have:

Name
Employee ID

Every employee must be able to:

Calculate their salary
Calculate their bonus

Full-time employees:
Have a monthly base salary.
Receive a 10% bonus based on their base salary.

Part-time employees:
Have an hourly rate.
Have the number of hours worked.
Salary depends on hours worked.
Do not receive a bonus.

Contractors:
Have a project payment.
Receive a 5% bonus based on the project payment.

System requirements
The system must be able to store different employee types together.
The payroll system must be able to process all employees without knowing their specific type.
Adding another employee type in the future should require minimal changes to existing code.
An employee must not be able to exist without the information required for its type.
Invalid salary-related values should be rejected.

OOP requirements
Your implementation must demonstrate:

Inheritance
Polymorphism
Encapsulation
Abstraction
Method overriding
Appropriate use of super()
Testing requirements

Create at least:

2 full-time employees
2 part-time employees
2 contractors

Then demonstrate:

Calculating each employee's salary
Calculating each employee's bonus
Processing all employees through the same payroll operation
At least 3 invalid-input cases
'''

from models import Employee, Full_time, Part_time, Contractor
from services import payroll_function

if __name__ == "__main__":
    f1 = Full_time("Batuhan", 12001, 20000)
    f2 = Full_time("Steve", 11701, 29000)

    p1 = Part_time("Hary", 67789, 200, 180)
    p2 = Part_time("Ahmed", 900001, 180, 190)

    c1 = Contractor("Merve", 18009, 35000)
    c2 = Contractor("Muhammed", 199998, 42000)

    for employee in Employee.employees:
        payroll_function(employee)