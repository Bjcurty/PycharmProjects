# def add(x,y):
#     print(x+y)
#
# add(5, 8)
# result = add(5, 8)
# # This will return None as functions return None by default
# print(result)

# def add(x,y):
#     # print(x+ y)
#     return x + y
#
# # add(5, 8)
# # result = add(5, 8)
# # print(result)
#
# print(add(5, 8))

# Not recommended to return different types of information
def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You ABSOLUTE UNIT!"

# This being multiplied by 5 will return 5 strings instead of doing math because of mixed return types
result = divide(15, 0)
print(result)