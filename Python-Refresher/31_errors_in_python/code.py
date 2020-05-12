def divide(dividend, divisor):
    if divisor == 0:
        # print("Divisor cannot be 0.")
        # return
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor


students = [
    {"name": "Bob", "grades": [75, 90]},
    {"name": "Rolf", "grades": [50]},
    {"name": "Jen", "grades": [100, 90]}
]

# divide(15, 0)

# grades = [78, 99, 85, 100]
grades = []

print("Welcome to the average grade program.")
try:
    # average = divide(sum(grades), len(grades))
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}.")
except ZeroDivisionError as e:
    # print("There are no grades yet in your list.")
    # print(e)
    print(f"ERROR: {name} has no grades!")
# except ValueError:
#     pass
else:
    # print(f"The average grade is {average}.")
    print("-- All student averages calculated --")
# This runs always
finally:
    # print("Thank you!")
    print("-- End of student average calculation --")


