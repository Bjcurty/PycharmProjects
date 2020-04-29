# # first class functions just mean that functions are variables
# def divide(dividend, divisor):
#     if divisor == 0:
#         raise ZeroDivisionError("Divisor cannot be 0.")
#
#     return dividend / divisor
#
#
# def calculate(*values, operator):
#     return operator(*values)
#
#
# # divide here is a first class function because it's being passed in to calculate
# result = calculate(20, 4, operator=divide)
# print(result)

from operator import itemgetter


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
        raise RuntimeError(f"Could not find an element with {expected}")


friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
]


def get_friend_name(friend):
    return friend["name"]


# print(search(friends, "Bob Smith", get_friend_name))
# print(search(friends, "Bob Smith", lambda friend: friend["name"]))
print(search(friends, "Bob Smith", itemgetter("name")))