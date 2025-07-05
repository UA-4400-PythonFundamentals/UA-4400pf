import re

def check_password(password):
    # Check length
    if len(password) < 6 or len(password) > 16:
        return False

    # Check for lowercase, uppercase, digit, and special character
    elif not re.search(r"[a-z]", password):
        return False
    elif not re.search(r"[A-Z]", password):
        return False
    elif not re.search(r"[0-9]", password):
        return False
    elif not re.search(r"[$#@]", password):
        return False
    
    return True

# Input from user
user_password = input("Enter your password: ")

if check_password(user_password):
    print("Valid password.")
else:
    print("Invalid password.")