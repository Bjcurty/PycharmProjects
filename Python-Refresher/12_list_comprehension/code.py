# List comprehension allows us to create new lists from old lists
# Pretty cool stuff
# numbers = [1, 3, 5]
# doubled = [x * 2 for x in numbers]
#
# # antiquated
# # for num in numbers:
# #     doubled.append(num * 2)
#
# print(doubled)

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]

# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)

print(friends)
print(starts_s)
print(friends is starts_s)
print("friends:", id(friends), "starts_s", id(starts_s))

