def count_characters(s):
    result = {}
    for char in s:
        result[char] = result.get(char, 0) + 1
    return result

input_str = "hello"
print(count_characters(input_str))

input_str = "Good buy"
print(count_characters(input_str))