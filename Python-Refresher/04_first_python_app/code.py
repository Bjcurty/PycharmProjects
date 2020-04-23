user_age = int(input("Enter your age(in years): "))
# years = int(user_age)
months = user_age * 12
seconds = months * 30 * 24 * 60 * 60
print(f"Your age, {user_age}, is equal to {months} months.")
print(f"Your age, {user_age}, is equal to {seconds} seconds.")