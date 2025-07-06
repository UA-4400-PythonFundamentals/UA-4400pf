#Task1. Write a function that returns the largest number of two numbers
#(use DocStrings documentation strings in the function).

def largest_number(a, b):
    """
    Returns the largest of two numbers after validating input types.
    If inputs are invalid, prints an error message and returns None.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float or None: The larger number, or None if input is invalid.
    """

    if not isinstance(a, (int,float)) or not isinstance(b, (int,float)):
        print("\tIt must be numbers!")
        return None

    return a if a > b else b 


print(largest_number(20, 10))
print(largest_number(-40, -4))
print(largest_number(15, 75.25))
print(largest_number(100, 100))
print(largest_number(50, "hello"))