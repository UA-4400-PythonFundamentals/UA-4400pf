class NegativeAgeError(Exception):
    pass


def process_age(age: int):

    if age < 0:
        raise NegativeAgeError("Age cannot be negative!")
    if age % 2 == 0:
        print(f"Your age is {age} — it's an even number.")
    else:
        print(f"Your age is {age} — it's an odd number.")


def task1():
    while True:
        s = input("\nEnter your age (or type 'back' to return to main menu): ")
        if s.lower() == 'back':
            print("Returning to main menu...")
            return
        if not s.isdigit() and not (s.startswith('-') and s[1:].isdigit()):
            print("Error: Please enter a valid integer number.")
            continue
        try:
            age = int(s)
            process_age(age)
        except NegativeAgeError as e:
            print("Exception:", e)


def task2():
    day_mapping = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    while True:
        s = input("\nEnter a number from 1 to 7 (or type 'back' to return to main menu): ")
        if s.lower() == 'back':
            print("Returning to main menu...")
            return
        if not s.isdigit():
            print("Error: Please enter a numeric value.")
            continue
        day_number = int(s)
        if day_number in day_mapping:
            print(f"{day_number} corresponds to {day_mapping[day_number]}")
        else:
            print("Error: Please enter a number between 1 and 7.")


def main_menu():
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Check age (even/odd)")
        print("2. Get day of the week from number")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            task1()
        elif choice == '2':
            task2()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")


# Entry point
if __name__ == "__main__":
    main_menu()