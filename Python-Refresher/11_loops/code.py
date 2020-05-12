number = 7
# user_input = input("Would you like to play? (Y/n) ").lower()

while True:
# while user_input != 'n':
    user_input = input("Would you like to play? (Y/n) ").lower()

    if user_input == 'n':
        break

    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You've guessed correctly!")
        break
    elif abs(number - user_number) == 1:
        print("You were only off by one!")
    else:
        print("Sorry Charlie, wrong number.")
    # user_input = input("Would you like to play? (Y/n) ").lower()

# friends = ["Rolf", "Jen", "Bob", "Anne"]
#
# # print(f"{friends[0]} is my friend")
# # print(f"{friends[1]} is my friend")
# # print(f"{friends[2]} is my friend")
# # print(f"{friends[3]} is my friend")
#
# for friend in friends:
#     print(f"{friend} is my friend")
#
# for friend in range(4):
#     print(f"{friend} is my friend")

# from statistics import mean
#
# grades = [35, 67, 98, 100, 100]
# # total = 0
# total = sum(grades)
# amount = len(grades)
# average = mean(grades)
#
# # for grade in grades:
# #     total += grade
#
# print(f"The average grade is {total / amount}.")
# print(f"The average grade is {average}.")
