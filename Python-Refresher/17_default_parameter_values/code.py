# # defaults can be set where they will be used if not overwritten by passed arguments
# # The defaults belong at the end of the arguments
# def add(x, y=8):
#     print(x+y)
#
# add(x=5)
# # can't give y a value only cuz x has no default
# # add(y=5)
# # can't do this either. No non default parameter before default
# # add(x=5, 5)

default_y = 3

def add(x, y=default_y):
    sum = x + y
    print(sum)

add(2)
# This change of default_y will not change the default in add because upon creation, it does not then further update
# this can become more confusing than it's worth
default_y = 4
add(2)