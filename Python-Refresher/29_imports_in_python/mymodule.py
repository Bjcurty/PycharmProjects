def divide(dividend, divisor):
    return dividend / divisor

# The __name__ is a global name in python that changes depending on which file you are in
# __ = "dunder"
print("mymodule.py: ", __name__)

import libs.mylib
