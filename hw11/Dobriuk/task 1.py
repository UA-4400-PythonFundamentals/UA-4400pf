class InputError(Exception):
    """Custom exception for incorrect age entry."""
    pass

def check(text: str) -> str:
    """
    Check the entered value and return a string
    with information if the age is even.

    :param text: what the user entered (string)
    :return: result string
    :raises InputError: if not integer or negative age is entered
    """
    try:
        age = int(text)
    except ValueError:
        raise InputError("Age must be an integer.")

    if age < 0:
        raise InputError("Age cannot be negative.")

    if age % 2 == 0:
        return "Your age is even."
    else:
        return "Your age is odd."

def main() -> None:
    """Main function."""
    user_input = input("Enter your age: ")
    try:
        result = check(user_input)
    except InputError as err:
        print("Error:", err)
    else:
        print(result)

if __name__ == "__main__":
    main()