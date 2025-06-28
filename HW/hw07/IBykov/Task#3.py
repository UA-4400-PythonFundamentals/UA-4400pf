def count_characters(s):

    result = {}
    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

user_input = input("Введіть рядок: ")
print("Символи та їх кількість:", count_characters(user_input))
