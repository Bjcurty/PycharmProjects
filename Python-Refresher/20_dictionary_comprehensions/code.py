# Much like list comprehension, but get a dictionary at the end instead
users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234")
]

# This becomes easier than creating a loop and doing if statements
username_mapping = {user[1]: user for user in users}

# print(username_mapping)
# print(username_mapping["Bob"])

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your details are correct!")
else:
    print("Your details are incorrect.")

