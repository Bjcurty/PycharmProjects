#  functions can take parameters

# def add(x, y):
#     result = x + y
#     print(result)
#
# add(5, 3)

# def say_hello():
#     print("Hello!")
#
# say_hello("Bob")

# positional arguments are important because they must be placed in position when called
# def say_hello(name):
#     print(f"Hello, {name}!")
#
# say_hello("Bob")
# # say_hello()

# def say_hello(name, surname):
#     print(f"Hello, {name} {surname}!")
#
# # say_hello("Bob", "Smith")
# # Keyword or named arguments allow order to be changed on arguments
# say_hello(surname="Bob", name="Smith")

# Use of keyword arguments allow code to be more readable
def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You ABSOLUTE UNIT!")

divide(divisor=15, dividend=0)