#Task1

def biggest_num(x,y) -> int:
    """
    Повертає більше з двох чисел.

    Аргументи:
    x -- перше число
    y -- друге число

    Повертає:
    int -- більше число

    """
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return 0
    
print(biggest_num(5, 10))  

