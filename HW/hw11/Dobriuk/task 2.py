class InputError(Exception):
    """Raised when thw user input is not an integer in the range 1-7"""
    pass

def check(text: str) -> str:
    """
    Convert the input string to an int and return the corresponding
    day of the week.
        1 → Monday, 2 → Tuesday, …, 7 → Sunday.

    Raises:
        InputError – if text is not an integer or is outside 1-7.
    """
    try:
        num = int(text)
    except ValueError:
        raise InputError("Input must be an integer.") from None
    
    if 1 <= num <= 7:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days[num - 1]
    else:
        raise InputError("Number must be between 1 and 7 (inclusive).") from None

if __name__ == "__main__":
    user_input = input("Enter a number from 1 to 7: ")
    try:
        print(check(user_input))
    except InputError as err:
        print(f"Error: {err}")