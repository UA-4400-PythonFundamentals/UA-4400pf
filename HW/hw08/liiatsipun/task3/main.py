from my_package.abc import area_of_rectangle, area_of_triangle, area_of_circle


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
