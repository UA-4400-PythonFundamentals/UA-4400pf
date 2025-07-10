import re


def validate_password(password):
    global validity
    validity = True
    if len(password) < 6 or len(password) > 16:
        print("Password must be between 6 and 16 characters long")
        validity = False
    if len(re.findall(r"[a-z]", password)) < 1:
        print("Password must contain at least one lowercase letter")
        validity = False
    if len(re.findall(r"[A-Z]", password)) < 1:
        print("Password must contain at least one uppercase letter")
        validity = False
    if len(re.findall(r"[0-9]", password)) < 1:
        print("Password must contain at least one digit")
        validity = False
    if len(re.findall(r"[#@]", password)) < 1:
        print("Password must contain at least one special character")
        validity = False
    if validity:
        print("Password is valid")
    return validity
