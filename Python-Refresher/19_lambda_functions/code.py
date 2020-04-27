# Operate on inputs and perform outputs, rarely used to perform actions
# def add(x, y):
#     return x + y

# lambda, list of parameters, return value
# short functions usually without name
# add = lambda x, y: x + y

# # Not usually used this way
# print((lambda x, y: x + y)(5, 7))
#
# # print(add(5, 7))

def double(x):
    return x * 2

sequence = [1, 3, 5, 9]
# doubled = [x * 2 for x in sequence]
# doubled = [double(x) for x in sequence]
# map goes over each element in list, set or tuple and performs the function on it
# doubled = map(double, sequence)
# # Map has to be turned into list to print
# print(list(doubled))
# # This is a little less clear
# doubled = [(lambda x: x * 2)(x) for x in sequence]
# This is a little easier to understand
doubled = list(map(lambda x: x * 2, sequence))
print(doubled)
