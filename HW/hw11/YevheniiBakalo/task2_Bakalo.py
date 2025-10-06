def get_day_by_number(number):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    if number in days:
        return f"The day is {days[number]}."
    else:
        return "Error: Number must be between 1 and 7."

def main():
    try:
        number = int(input("Enter a number (1–7): "))
        print(get_day_by_number(number))
    except ValueError:
        print("Error: Please enter a valid number.")

if __name__ == "__main__":
    main()