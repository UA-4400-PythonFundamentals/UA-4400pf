def get_day_of_week(num):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    if num not in days:
        raise ValueError("Number must be between 1 and 7 to represent a day of the week.")
    return days[num]

def main():
    try:
        user_input = input("Enter a number (1-7) to get the day of the week: ")
        num = int(user_input)
        day = get_day_of_week(num)
        print(f"The day corresponding to {num} is {day}.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception:
        print("Error: Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()