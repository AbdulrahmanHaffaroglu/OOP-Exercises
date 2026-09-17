from .employees import Employee

class Part_time(Employee):
    def __init__(self, name, emp_id, hr_rate, work_hrs):

        if hr_rate < 0:
            raise ValueError("hour rate cant be negative")
        
        if work_hrs < 0:
            raise ValueError("worked hours cant be negative")

        
        super().__init__(name, emp_id)
        self._hr_rate = hr_rate
        self._work_hrs = work_hrs


    def clc_salary(self):
        return self._hr_rate * self._work_hrs

    def clc_bonus(self):
        return 0


    # getter functions
    def hr_rate_getter(self):
        return self._hr_rate

    def work_hrs_getter(self):
        return self._work_hrs


    # setter functions
    def hr_rate_setter(self, hr_rate):
        if hr_rate < 0:
            raise ValueError("hour rate cant be negative")
        
        self._hr_rate = hr_rate


    def work_hrs_setter(self, work_hrs):
        if work_hrs < 0:
            raise ValueError("work hours cant be negative")
                
        self._work_hrs = work_hrs



    
    #assigning properties
    hr_rate = property(fset=hr_rate_setter, fget=hr_rate_getter)
    work_hrs = property(fset=work_hrs_setter, fget=work_hrs_getter)