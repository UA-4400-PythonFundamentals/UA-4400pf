import math

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def area_circle(radius):
    return math.pi * radius ** 2

def main():
    print("Виберіть фігуру:")
    print("1 - Прямокутник")
    print("2 - Трикутник")
    print("3 - Коло")
    choice = input("Введіть 1, 2 або 3: ")
    if choice == '1':
        l = float(input("Довжина: "))
        w = float(input("Ширина: "))
        print(f"Площа прямокутника: {area_rectangle(l, w):.2f}")
    elif choice == '2':
        b = float(input("Основа: "))
        h = float(input("Висота: "))
        print(f"Площа трикутника: {area_triangle(b, h):.2f}")
    elif choice == '3':
        r = float(input("Радіус: "))
        print(f"Площа кола: {area_circle(r):.2f}")
    else:
        print("Невірний вибір.")

main()
