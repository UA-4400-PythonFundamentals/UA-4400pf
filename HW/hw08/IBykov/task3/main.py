from areas import rectangle_area, triangle_area, circle_area


def main():
    print("Калькулятор площ фігур")
    print("1. Прямокутник")
    print("2. Трикутник")
    print("3. Коло")

    while True:
        choice = input("\nВиберіть фігуру (1-3): ")

        if choice == '1':
            a = float(input("Введіть довжину прямокутника: "))
            b = float(input("Введіть ширину прямокутника: "))
            area = rectangle_area(a, b)
            print(f"Площа прямокутника: {area}")

        elif choice == '2':
            h = float(input("Введіть висоту трикутника: "))
            a = float(input("Введіть основу трикутника: "))
            area = triangle_area(h, a)
            print(f"Площа трикутника: {area}")

        elif choice == '3':
            r = float(input("Введіть радіус кола: "))
            area = circle_area(r)
            print(f"Площа кола: {area}")

        else:
            print("Неправильний вибір! Виберіть 1, 2 або 3.")


if __name__ == "__main__":
    main()