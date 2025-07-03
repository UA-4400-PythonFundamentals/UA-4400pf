def count_chars(s):
    result = {}
    for char in s:
        result[char] = result.get(char, 0) + 1
    return result

print(count_chars("hello"))
