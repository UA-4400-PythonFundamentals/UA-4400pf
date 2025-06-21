import math

def area_of_rectangle(a, b):
    return a * b

def area_of_triangle(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s

def area_of_circle(r):
    return math.pi * r ** 2


def main():
    choice = input("Що обчислювати? (rectangle / triangle / circle): ").lower()

    if choice == "rectangle":
        a = float(input("Введи довжину: "))
        b = float(input("Введи ширину: "))
        print("Площа прямокутника:", area_of_rectangle(a, b))

    elif choice == "triangle":
        a = float(input("Введи a: "))
        b = float(input("Введи b: "))
        c = float(input("Введи c: "))
        print("Площа трикутника:", area_of_triangle(a, b, c))

    elif choice == "circle":
        r = float(input("Введи радіус: "))
        print("Площа кола:", area_of_circle(r))

    else:
        print("Невірний вибір.")

main()
