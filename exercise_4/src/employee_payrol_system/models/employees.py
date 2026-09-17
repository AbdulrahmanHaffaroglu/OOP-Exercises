from abc import ABC, abstractmethod

class Employee(ABC):

    employees = []

    def __init__(self, name, emp_id):
        if emp_id < 0:
            raise ValueError("id cant be negative")
        
        self.name = name
        self.emp_id = emp_id
        Employee.employees.append(self)

    @abstractmethod
    def clc_salary(self):
        pass

    @abstractmethod
    def clc_bonus(self):
        pass