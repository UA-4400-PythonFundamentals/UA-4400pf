from areas import area_rectangle, area_triangle, area_circle


def get_float(prompt: str) -> float:
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("Неправильне значення. Будь ласка, введіть числове значення.")


def main():
    while True:
        print("\nОберіть фігуру для обчислення площі:")
        print("  1) Прямокутник")
        print("  2) Трикутник")
        print("  3) Коло")
        print("  4) Вихід")
        choice = input("Введіть 1, 2, 3 або 4: ").strip()

        if choice == "1":
            a = get_float("Введіть сторону a: ")
            b = get_float("Введіть сторону b: ")
            result = area_rectangle(a, b)
            shape = "прямокутника"

        elif choice == "2":
            h = get_float("Введіть висоту: ")
            base = get_float("Введіть основу: ")
            result = area_triangle(h, base)
            shape = "трикутника"

        elif choice == "3":
            r = get_float("Введіть радіус: ")
            result = area_circle(r)
            shape = "кола"

        elif choice == "4":
            print("До побачення!")
            break

        else:
            print("Невірний вибір. Будь ласка, введіть 1, 2, 3 або 4.")
            continue

        print(f"Площа {shape} становить {result:.2f}")


if __name__ == "__main__":
    main()