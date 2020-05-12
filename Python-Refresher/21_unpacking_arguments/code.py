# # using the * here will take all arguments
# def multiply(*args):
#     # print(args)
#     total = 1
#     for arg in args:
#         total *= arg
#
#     return total
#
# # print(multiply(1, 3, 5))
# print(multiply(-1))

# def add(x, y):
#     return x + y
#
# # nums = [3, 5]
# nums = {"x": 15, "y": 25}
# chars = {"x": "x", "y": "y"}
# # using * here destructures the list into arguments to then pass into the function
# # print(add(*nums))
# # print(add(x=3, y=5))
# # print(add(nums["x"], nums["y"]))
# # print(add(x=nums["x"], y=nums["y"]))
# # The ** in this case will go into the dictionary and then take the value from each keyed pair to add
# print(add(**nums))
# print(add(**chars))

def multiply(*args):
    # print(args)
    total = 1
    for arg in args:
        total *= arg

    return total

# This calls for arguments to be passed in and also an operator.
# Arguments must be passed in first and then operator last
def apply(*args, operator):
    if operator == "*":
        # args needs the * in front of it because in current form, it is a tuple
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."

print(apply(1, 3, 6, 7, operator="+"))
print(apply(1, 3, 6, 7, operator="*"))

