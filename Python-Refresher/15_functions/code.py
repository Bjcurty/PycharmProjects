# calling, running or executing a function all mean the same thing
# def hello():
#     print("Hello!")
#
# hello()

# def user_age_in_seconds():
#     user_age = int(input("Enter your age: "))
#     age_seconds = user_age * 365 * 24 * 60 * 60
#     print(f"Your age in seconds is {age_seconds}.")
#
# print("Welcome to the age in seconds program!")
# user_age_in_seconds()
#
# print("Goodbye!")

# Usually don't want to redefine python native functions
# def print():
#     print("Hello, world!")
#
# print()

# friends = ["Rolf", "Bob"]
#
# this creates confusion as to which friends the program is using kind of like x = x + 5 where x doesn't yet exist
# def add_friends():
#     friend_name = input("Enter your friend name: ")
#     friends = friends + [friend_name]
#
# add_friends()

# # can't call a function before it's been created
# say_hello()
#
# def say_hello():
#     print("Hello!")

# even though you can do this, better practice is to define global variables before using them in a def
# since line 43 runs before this def being called in 44, this will work
def add_friend():
    friends.append("Rolf")

friends = []
add_friend()

print(friends)    #[Rolf]