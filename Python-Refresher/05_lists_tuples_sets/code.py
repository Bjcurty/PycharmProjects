# Lists can have elements added and removed
l = ["Bob", "Rolf", "Anne"]
# Tuples cannot be added to or removed from after creation
# Tuples need to have a , after first value
# can state a single value tuple as t = 15, without the parenthesis
t = ("Bob", "Rolf", "Anne")
# Sets can be added to or removed from, but don't guarantee order
s = {"Bob", "Rolf", "Anne"}

# Subscript notation is good for lists and tuples
print(t[2])

l[0] = "Smith"
print(l)

# adds something to a list
l.append("Smith")
print(l)

l.remove("Rolf")
print(l)

s.add("Smith")
print(s)