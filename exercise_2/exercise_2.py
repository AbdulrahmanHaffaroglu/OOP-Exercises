'''
Create a Student class:

Student
 ├── name
 ├── student_id
 └── grades

Methods:

add_grade(grade)
average_grade()
highest_grade()
is_passing()

Then create multiple students and determine who has the highest average.

Extra challenge: Don't allow grades outside 0–100.
'''

class Student:
    def __init__(self, name, student_id, grades):
        self.name = name
        self._student_id = student_id
        self._grades = [grade for grade in grades if grade <= 100 and grade >= 0]

    def add_grade(self, grade):
        if grade < 0 or grade > 100:
            raise ValueError("grade should be between 0 and 100")

        self._grades.append(grade)

    def average_grade(self):
        if not self._grades:
            return 0
        
        return sum(self._grades) / len(self._grades)

    def highest_grade(self):
        if not self._grades:
            return None
        
        return max(self._grades)

    def is_passing(self):
        return self.average_grade() >= 50

def highest_average(students):
    high = 0
    name = ''

    for student in students:
        if student.average_grade() > high:
            high = student.average_grade()
            name = student.name

    return name, high


if __name__ == '__main__':
    s1 = Student('Muhammed', 111, [40, 50])
    s2 = Student('Ali', 112, [90, 100, 80])
    s3 = Student('Yusuf', 113, [80, 20, 89])

    for grade in [101, 90]:
        try:
            s1.add_grade(grade)
        except ValueError as e:
            print(f"Error: {e}")

    s1.add_grade(90)

    print(s1.highest_grade())
    print(s3.is_passing())

    print(s1.average_grade())
    print(s2.average_grade())
    print(s3.average_grade())

    students = [s1, s2, s3]

    name, high = highest_average(students)

    print(f"student {name} has the highest average {high}")