import os
import sys
from rectangle import Rectangle
from human_module import Human
from employee_module import Employee

BANNER = r"""
############################################
#           DEMO PROGRAM MENU              #
############################################
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    clear_screen()
    print(BANNER)
    print("1: Rectangle Demo")
    print("2: Human Demo")
    print("3: Employee Demo")
    print("0: Exit")

def rectangle_demo():
    while True:
        try:
            w = float(input("\nВведіть ширину прямокутника: "))
            h = float(input("Введіть висоту прямокутника: "))
            rect = Rectangle(w, h)
            print(rect)
            print(f"Площа: {rect.area}")
            print(f"Периметр: {rect.perimeter}")
        except Exception as e:
            print(f"Помилка: {e}")
        again = input("\nЗапустити знову цей розділ? (r для повторення, будь-яка інша — назад): ")
        if again.lower() != 'r':
            break

def human_demo():
    while True:
        name = input("\nВведіть ім'я людини: ")
        try:
            person = Human(name)
            person.greet()
            print(Human.species_info())
            print("Повідомлення дня:", Human.random_message())
        except Exception as e:
            print(f"Помилка: {e}")
        again = input("\nЗапустити знову цей розділ? (r для повторення, будь-яка інша — назад): ")
        if again.lower() != 'r':
            break

def employee_demo():
    # Скидаємо приклади
    Employee._employees.clear()
    Employee._employee_count = 0
    Employee("Іван Петренко", 700.0)
    Employee("Ольга Шевченко", 1200.5)
    Employee("Марія Іванова", 950.0)
    while True:
        print("\n1: Показати всіх співробітників")
        print("2: Підвищити заробітну плату")
        print("3: Інспекція класу Employee")
        print("r: Перезапустити розділ")
        print("b: Назад до головного меню")
        choice = input("Ваш вибір: ")
        if choice == "1":
            Employee.display_all_employees()
        elif choice == "2":
            name = input("Ім'я співробітника для підвищення: ")
            try:
                percent = float(input("Відсоток підвищення: "))
                for emp in Employee._employees:
                    if emp.name == name:
                        emp.give_raise(percent)
                        break
                else:
                    print("Співробітника не знайдено.")
            except Exception as e:
                print(f"Помилка: {e}")
        elif choice == "3":
            print("\n--- Інспекція класу Employee ---")
            print("Базові класи (__bases__):", Employee.__bases__)
            print("Імена атрибутів у просторі імен (__dict__.keys()):", list(Employee.__dict__.keys()))
            print("Ім'я класу (__name__):", Employee.__name__)
            print("Модуль (__module__):", Employee.__module__)
            print("Докстрінг (__doc__):", Employee.__doc__)
        elif choice.lower() == 'r':
            return employee_demo()
        elif choice.lower() == 'b':
            break
        else:
            print("Невірний вибір.")

def main():
    while True:
        print_menu()
        choice = input("\nОберіть опцію: ")
        if choice == "1":
            rectangle_demo()
        elif choice == "2":
            human_demo()
        elif choice == "3":
            employee_demo()
        elif choice == "0":
            print("До побачення!")
            sys.exit(0)
        else:
            print("Невірний вибір.")

if __name__ == "__main__":
    main()