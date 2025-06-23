def calc_letters(word):
    letters = {}
    for l in word:
        letters[l] = word.count(l)
    print(letters)

word = input("Provide word to count letters: ")
word = word.lower()
calc_letters(word)