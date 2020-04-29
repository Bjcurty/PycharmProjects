import functools

user = {"username": "jose", "access_level": "guest"}


# This function is called a decorator
# def make_secure(func):
#     # This will allow the original function to keep documentation associated with it
#     @functools.wraps(func)
#     # This is not a decorator, just the function that will replace the old
#     def secure_function():
#         if user["access_level"] == "admin":
#             return func()
#         else:
#             return f"No admin permissions for {user['username']}"
#
#     return secure_function


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}"

    return secure_function


# This prevents function from being created as is and forces the above function to work
# This causes get_admin_password to no longer be registered internally as a function
# @make_secure
# def get_admin_password():
#     return "1234"


@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"


# print(get_admin_password())
# print(get_admin_password.__name__)
print(get_password("billing"))
