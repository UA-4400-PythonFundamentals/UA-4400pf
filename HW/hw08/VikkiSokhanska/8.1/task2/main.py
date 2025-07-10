def is_valid_password(password):
    if len(password) < 6 or len(password) > 16:
        return False

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "$#@" for c in password)

    return has_lower and has_upper and has_digit and has_special

password = input("Enter your password: ")

if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid.")
