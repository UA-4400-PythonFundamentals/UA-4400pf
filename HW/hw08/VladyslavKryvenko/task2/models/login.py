def validation_password(password):
    if not (5 < len(password) < 17):
        print("Password length must be between 6 and 15 characters.")
        return False

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in '#$@' for c in password)

    if all([has_lower, has_upper, has_digit, has_special]):
        return True
    else:
        _massage()
        return False


def _massage():
    print('''        Password Validation Rules:
    At least 1 lowercase letter between [a-z]
    At least 1 uppercase letter between [A-Z]
    At least 1 number between [0-9]
    At least 1 character from [$#@]
    Minimum length: 6 characters
    Maximum length: 16 characters''')
    