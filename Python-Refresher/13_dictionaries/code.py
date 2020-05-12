# dictionaries are used to associate key and value pairs
# hashable types are ints or strings
# friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
#
# friend_ages["Bob"] = 20
#
# # print(friend_ages["Adam"])
#
# print(friend_ages)

# friends = [
#     {"name": "Rolf", "age": 24},
#     {"name": "Adam", "age": 30},
#     {"name": "Anne", "age": 27}
# ]
#
# print(friends[1]["name"])

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

# for student in student_attendance:
#     print(f"{student}: {student_attendance[student]}")

# better
# for student, attendance in student_attendance.items():
#     print(f"{student}: {attendance}")

# if "Bob" in student_attendance:
#     print(f"Bob: {student_attendance['Bob']}")
# else:
#     print("Bob is not a student in this class.")

attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))