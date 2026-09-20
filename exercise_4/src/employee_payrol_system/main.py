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