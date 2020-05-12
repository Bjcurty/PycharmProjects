# name = "Bob"
# # greeting = "Hello, Bob"
# greeting = f"Hello, {name}"
#
# # print(greeting)
# print(f"Hello, {name}")
#
# name = "Rolf"
#
# # print(greeting)
# print(f"Hello, {name}")

# name = "Bob"
# greeting = "Hello, {}"
# with_name = greeting.format(name)
# with_name_two = greeting.format("Rolf")
#
# print(with_name)
# print(with_name_two)

longer_phrase = "Hello, {}. Today is {}."

formatted = longer_phrase.format("Rolfe", "Monday")
print(formatted)