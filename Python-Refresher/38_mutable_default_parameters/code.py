from typing import List, Optional


class Student:
    # self.grades will be a list that both bob and rolf are added to
    # def __init__(self, name: str, grades: List[int] = []):  # This is bad!
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        self.name = name
        # self.grades = grades
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)
