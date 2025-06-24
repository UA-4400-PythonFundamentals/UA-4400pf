num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

def find_bigger_number(num1, num2):
    """
    Returns the larger of the two numbers
    """
    if num1 > num2:
        return num1
    else:
        return num2

print(find_bigger_number(num1, num2))
