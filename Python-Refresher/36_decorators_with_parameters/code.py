import functools

user = {"username": "jose", "access_level": "guest"}


# can improve logic by setting access_levels to int and then number logic can be used
def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}"

        return secure_function
    return decorator


@make_secure("admin")
def get_admin_password():
    return "admin: 123"


@make_secure("user")
def get_dashboard_password():
    return"user: user_password"


print(get_admin_password())
print(get_dashboard_password())

user = {"username": "anna", "access_level": "admin"}

print(get_admin_password())
print(get_dashboard_password())