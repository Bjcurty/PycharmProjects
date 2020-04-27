# student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}
#
# def average(sequence):
#     return sum(sequence) / len(sequence)
#
# # The function knows nothing about the student
# print(average(student["grades"]))
# # This approach takes object oriented programming
# # print(student.average())

# class Student:
#     # important for instantiation (method because its inside a class)
#     def __init__(self):
#         self.name = "Rolf"
#         self.grades = (90, 90, 93, 78, 90)
#
#     def average_grade(self):
#         return sum(self.grades) / len(self.grades)
#
# student = Student()
# print(student.name)
# print(student.grades)
# # print(Student.average(student))
# print(student.average_grade())

# class Student:
#     # important for instantiation (method because its inside a class)
#     def __init__(self, name):
#         self.name = name
#         self.grades = (90, 90, 93, 78, 90)
#
#     def average_grade(self):
#         return sum(self.grades) / len(self.grades)
#
# student = Student("Bob")
# print(student.name)
# print(student.grades)
# print(student.average_grade())

class Student:
    # important for instantiation (method because its inside a class)
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob", (100, 100, 93, 78, 90))
student2 = Student("Rolfe", (90, 90, 93, 78, 90))
print(student.name)
print(student.grades)
print(student.average_grade())

print(student2.name)
print(student2.grades)
print(student2.average_grade())