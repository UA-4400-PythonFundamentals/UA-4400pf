def rectangle_area(length, width):

    return length * width

def triangle_area(base, height):

    return 0.5 * base * height

def circle_area(radius):

    pi = 3.14
    return pi * radius * radius

print("Оберіть фігуру для обчислення площі:")
print("1. Прямокутник")
print("2. Трикутник")
print("3. Коло")

choice = input("Введіть номер фігури (1/2/3): ")

if choice == "1":
    l = float(input("Введіть довжину прямокутника: "))
    w = float(input("Введіть ширину прямокутника: "))
    print("Площа прямокутника:", rectangle_area(l, w))

elif choice == "2":
    b = float(input("Введіть основу трикутника: "))
    h = float(input("Введіть висоту трикутника: "))
    print("Площа трикутника:", triangle_area(b, h))

elif choice == "3":
    r = float(input("Введіть радіус кола: "))
    print("Площа кола:", circle_area(r))

else:
    print("Невірний вибір.")
