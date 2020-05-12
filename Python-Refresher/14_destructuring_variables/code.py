# destructuring makes code a lot more readable
# x = 5
# x = (5, 11)
# parenthesis are actually only needed when putting tuples into a list so they aren't confused with that list
# x = 5, 11
# x, y = 5, 11
# t = 5,11
# x, y = t
#
# print(x,y)

# student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
#
# print(list(student_attendance.items()))
#
# # for student, attendance in student_attendance.items():
# #     print(f"{student}: {attendance}")
#
# for t in student_attendance.items():
#     print(t)

# people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]
#
# for name, age, profession in people:
#     print(f"Name: {name}, Age: {age}, Profession: {profession}")

# _ variable is meant to be ignored
# person = ("Bob", 42, "Mechanic")
# name, _, profession = person
#
# print(name, profession)

# * gives a trailing value when destructuring a variable
# head, *tail = [1, 2, 3, 4, 5]
# print(head)
# print(tail)

*head, tail = [1, 2, 3, 4, 5]
print(head)
print(tail)