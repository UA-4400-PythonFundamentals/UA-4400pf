def find_max():
    """
    Повертає більше з двох чисел.

    Параметри:
    num_1 (int або float): перше число
    num_2 (int або float): друге число

    Повертає:
    int або float: більше з двох чисел
    """
    num_1 = int(input("Введіть перше число: "))
    num_2 = int(input("Введіть друге число: "))
    if num_1 > num_2:
        return num_1
    else:
        return num_2
print(f"Найбільше число - це {find_max()}")