def number_of_char():
    word = input("Введіть слово: ")
    result = {}

    for letter in word:
        result[letter] = result.get(letter, 0) + 1

    print(result)
number_of_char()