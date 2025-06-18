def largest_number():
    """
    Returns the largest of two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The larger number.
    """
    num1 = int(input("Please enter the first number:"))
    num2 = int(input("Please enter the second number"))

    if num1 > num2:
        return num1
    elif num1 == num2:
        return None
    else:
        return num2


print(f"The largest number is {largest_number()}")
