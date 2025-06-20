def count_of_char():
    str = input("Please enter the string:")
    result = {}

    for char in str:
        result[char] = result.get(char, 0) + 1

    return result


print(count_of_char())
