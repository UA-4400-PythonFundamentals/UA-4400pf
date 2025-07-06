def is_valid_password(password):
    if not (6 <= len(password) <= 16):
        return False

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for ch in password:
        if 'a' <= ch <= 'z':
            has_lower = True
        elif 'A' <= ch <= 'Z':
            has_upper = True
        elif '0' <= ch <= '9':
            has_digit = True
        elif ch in "$#@":
            has_special = True

    return has_lower and has_upper and has_digit and has_special

if __name__ == "__main__":
    password = input("Enter your password: ")
    if is_valid_password(password):
        print("Valid password!")
    else:
        print("Invalid password.")