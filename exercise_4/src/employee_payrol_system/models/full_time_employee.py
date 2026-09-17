from .employees import Employee

class Full_time(Employee):
    def __init__(self, name, emp_id, mth_base_slr):
        if mth_base_slr < 0:
            raise ValueError("Salary can't be a negative number")

        super().__init__(name, emp_id)
        self._mth_base_slr = mth_base_slr


    def clc_salary(self):
        return self._mth_base_slr

    def clc_bonus(self):
        return self._mth_base_slr / 10 # 10 percent of salary


    # salary getter
    def slr_getter(self):
        return self._mth_base_slr
    
    # the clc_salary does the same thing as the getter function,
    # but in a real life scenario it's better to seperate them from each other
    # because the company in the scenario maybe decides a different way to calculate the salary in the future 



    # salary setter
    def slr_setter(self, mth_base_slr):
        if mth_base_slr >= 0:
            self._mth_base_slr = mth_base_slr
        else:
            raise ValueError("salary cant be a negative number")

    mth_base_slr = property(fset=slr_setter, fget=slr_getter)