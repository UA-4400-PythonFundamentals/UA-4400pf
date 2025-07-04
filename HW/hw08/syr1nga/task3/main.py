from areas import rectangle, circle, triangle

def main():
    print("Оберіть фігуру для обчислення площі: ")
    print("1. Прямокутник")
    print("2. Трикутник")
    print("3. Коло")

    choice = input("Введіть свій вибір (1/2/3): ")

    if choice == '1':
        l = int(input("Довжина: "))
        w = int(input("Ширина: "))
        area = rectangle(l, w)
        print(f"Площа прямокутника: {area}")
    elif choice == '2':
        b = int(input("Основа: "))
        h = int(input("Висота: "))
        area = triangle(h, b)
        print(f"Площа трикутника: {area}")
    elif choice == '3':
        r = int(input("Радіус: "))
        area = circle(r)
        print(f"Площа кола: {area}")
    else:
        print("Я не знаю інших фігур :(")

main()