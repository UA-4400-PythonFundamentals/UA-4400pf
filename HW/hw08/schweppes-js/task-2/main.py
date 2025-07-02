import re

def is_valid_password(password):
    pattern = re.compile(
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,16}$"
    )
    return bool(pattern.match(password))

user_password = input("Enter your password: ")

if is_valid_password(user_password):
    print("Password is valid")
else:
    print("Password is invalid")
