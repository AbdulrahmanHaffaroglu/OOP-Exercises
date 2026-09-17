from .employees import Employee

class Contractor(Employee):
    def __init__(self, name, emp_id, prjt_pay):
        if prjt_pay < 0:
            raise ValueError("payment cant be negative")
        super().__init__(name, emp_id)
        self._prjt_pay = prjt_pay

    def clc_salary(self):
        return self._prjt_pay

    def clc_bonus(self):
        return self._prjt_pay / 20 # 5 percent of salary

    # setter function
    def prjt_pay_setter(self, prjt_pay):
        if prjt_pay < 0:
            raise ValueError("payment cant be negative")
        self._prjt_pay = prjt_pay

    prjt_pay = property(fset=prjt_pay_setter, fget=clc_salary)
