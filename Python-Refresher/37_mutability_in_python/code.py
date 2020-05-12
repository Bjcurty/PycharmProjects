# all things in python are mutable unless being set up to not be
# tuples, ints, strings, floats, booleans
# for a class to be immutable, it needs to not be changeable by the methods

# a = []
# b = []
#
# a = ()
# b = ()

# a.append(35)
#
# print(a)
# print(b)

# python doesn't recreate numbers that have already been created
# a = 85798
# b = 85798
#
# print(id(a))
# print(id(b))
#
# a = 8598

a = "hello"
b = a

print(id(a))
print(id(b))

a += " world"

print(id(a))
