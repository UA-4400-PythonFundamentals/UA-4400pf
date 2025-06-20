def max_of_two(a, b):
    """
    Returns the largest of two numbers.

    Parameters:
    a (int): First number.
    b (int): Second number.

    Returns:
    int: The larger of the two numbers.
    """
    return a if a > b else b

# extra test program
def get_integer(prompt):
    """
    Asks the user for an integer input and keeps asking if the user didn't input an integer.

    Parameters:
    prompt (str): The prompt message to display to the user.

    Returns:
    int: A valid integer entered by the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter an integer.")


# Main part of the program
def main():
    print("Note: number must be an integer.")
    num1 = get_integer("Enter the first (1) number: ")
    num2 = get_integer("Enter the second (2) number: ")

    largest = max_of_two(num1, num2)
    print(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()