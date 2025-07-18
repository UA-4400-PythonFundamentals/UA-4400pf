import math

def max_of_two(a, b):
    return a if a >= b else b


def area_rectangle(width, height):
    return width * height


def area_triangle(base, height):
    return (base * height) / 2


def area_circle(radius):
    return math.pi * radius ** 2


def count_chars(s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    return counts


def input_float(prompt):
    raw = input(prompt)
    raw = raw.strip().replace(',', '.')
    return float(raw)


def main():
    while True:
        print("\n=== Головне меню ===")
        print("1) Знайти найбільше з двох чисел")
        print("2) Обчислити площу (прямокутник, трикутник, коло)")
        print("3) Порахувати символи у рядку")
        print("4) Вихід")
        choice = input("Виберіть опцію (1-4): ")

        if choice == '1':
            a = input_float("Введіть перше число: ")
            b = input_float("Введіть друге число: ")
            print(f"Найбільше число: {max_of_two(a, b)}")

        elif choice == '2':
            print("a) Прямокутник")
            print("b) Трикутник")
            print("c) Коло")
            shape = input("Виберіть фігуру (a-c): ")

            if shape == 'a':
                w = input_float("Ширина прямокутника: ")
                h = input_float("Висота прямокутника: ")
                print(f"Площа прямокутника: {area_rectangle(w, h)}")
            elif shape == 'b':
                base = input_float("Основa трикутника: ")
                h = input_float("Висота трикутника: ")
                print(f"Площа трикутника: {area_triangle(base, h)}")
            elif shape == 'c':
                r = input_float("Радіус кола: ")
                print(f"Площа кола: {area_circle(r)}")
            else:
                print("Невірний вибір фігури.")

        elif choice == '3':
            s = input("Введіть рядок: ")
            result = count_chars(s)
            print("Кількість символів:", result)

        elif choice == '4':
            print("До побачення!")
            break

        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == '__main__':
    main()