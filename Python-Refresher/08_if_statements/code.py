day_of_week = input("What day of the week is it today?").lower()

if day_of_week == "monday":
    # python programming requires indentation (4 spaces is a good standard)
    print("Have a great start to your week you Oh My Lantas!")
elif day_of_week == "tuesday":
    print("Es ist Dienstag.")
else:
    print("CHOO CHOO MOTHA TRUCKAS!")
# This is inefficient, use else/elif
# if day_of_week != "Monday":
#     print("Choo choo mother truckers")

print("This always runs.")