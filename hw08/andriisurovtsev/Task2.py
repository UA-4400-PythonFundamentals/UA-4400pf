# task2
import re

def valid_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    return True
user_password = input("Enter a password: ")

if valid_password(user_password):
    print("Password is valid")
else:
    print("Password is not valid")