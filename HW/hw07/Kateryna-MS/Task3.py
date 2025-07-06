def char_number():
    '''calculates the number of characters included in given string'''
    text = input()
    result = {}
    for character in text:
        result[character] = result.get(character,0) +1
    print(result)
