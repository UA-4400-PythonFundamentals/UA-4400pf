def calculates_of_characters(str1):
    str1 = str1.lower()
    count = {}
    for i in str1:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    return count


str1 = input("Введи стрічку: ")
print(calculates_of_characters(str1))
