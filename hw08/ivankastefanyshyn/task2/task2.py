import re


def validity_of_password(password):
    """
    Validate password based on length, case, digit, and special char.

    Args:
        password (str): Password to validate.

    Returns:
        True if valid, otherwise an error message string.
    """
    if len(password) < 6 or len(password) > 16:
        return "Sorry, the length of the password should be between 6 and 16 characters"
    elif not re.search("[a-z]", password):
        return "Sorry, the password should have at least 1 letter between [a-z]"
    elif not re.search("[A-Z]", password):
        return "Sorry, the password should have at least 1 letter between [A-Z]"
    elif not re.search("[0-9]", password):
        return "Sorry, the password should have at least 1 number between [0-9]"
    elif not re.search("[$#@]", password):
        return "Sorry, the password should have at least 1 character from [$#@]"
    return True


while True:
    password = input("Please enter your password:")
    result = validity_of_password(password)
    if result is True:
        print("Your password is valid")
        break
    else:
        print(result)
