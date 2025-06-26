def charCount(text):
    """
    Counts the number of each character in a given string.
    """
    result = {}
    for char in text.lower():
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result
word = "hello"
print(charCount(word))