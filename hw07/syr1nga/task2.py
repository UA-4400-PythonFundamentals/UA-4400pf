def rectangle(l, w):
    """
    Calculates the area of a rectangle.
    """
    return l * w

def triangle(b, h):
    """
    Calculates the area of a triangle.
    """
    return 0.5 * b * h

def circle(r):
    """
    Calculates the area of a circle.
    """
    pi = 3.14159
    return pi * r ** 2

def main():
    print("Оберіть фігуру для обчислення площі: ")
    print("1. Прямокутник")
    print("2. Трикутник")
    print("3. Коло")

    choice = input("Введіть свій вибір (1/2/3): ")

    if choice == '1':
        l = int(input("Довжина: "))
        w = int(input("Ширина: "))
        print(f"Площа прямокутника: {rectangle(l, w)}")
    elif choice == '2':
        b = int(input("Основа: "))
        h = int(input("Висота: "))
        print(f"Площа трикутника: {triangle(b, h)}")
    elif choice == '3':
        r = int(input("Радіус: "))
        print(f"Площа кола: {circle(r):.2f}")
    else:
        print("Я не знаю інших фігур :(")

main()