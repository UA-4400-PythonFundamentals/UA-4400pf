def max_of_two(a, b):

    if a > b:
        return a
    else:
        return b

num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
print("Більше число:", max_of_two(num1, num2))
