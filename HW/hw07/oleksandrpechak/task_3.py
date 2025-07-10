# Напиши функцію, яка обчислює кількість символів у заданому рядку.
def char(word: str) -> dict:
    word = word.lower()
    counter = {}
    for i in str(word):
       counter[i]= counter.get(i, 0) +1
       return counter
text = "Hello"
print(char(text))