def largest_number(num1, num2):
    """
    Return the largest of two given numbers.

    Args:
        num1: First number to compare
        num2: Second number to compare

    Returns:
        The larger of the two input numbers.
        If numbers are equal, returns num1.
    """
    return num1 if num1 > num2 else num2

