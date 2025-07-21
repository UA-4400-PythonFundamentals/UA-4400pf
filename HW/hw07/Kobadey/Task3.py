def charCounter(line):
    '''Count the number of characters in a line'''
    charCount = {}
    for char in line:
        charCount[char] = charCount.get(char, 0) + 1
    return charCount

myString = input("Enter a string: ")
print(charCounter(myString))
