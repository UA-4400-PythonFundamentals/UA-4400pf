def count_characters(s_string):
    """
    Calculates the number of characters included in given string.

    Parameters:
    s_string (str): Input string.

    Returns:
    dict: A dictionary with characters as keys and their counts as values.
    """
    result = {}
    for char in s_string:
        if char not in result:
            result[char] = s_string.count(char)
    return result

# Example usage:
print(count_characters("hello"))  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
