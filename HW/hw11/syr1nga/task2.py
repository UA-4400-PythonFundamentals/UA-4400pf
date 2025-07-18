def week(number):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    if number < 1 or number > 7:
        raise ValueError("Number must be between 1 and 7.")
    
    return days[number]

def main():
    try:
        user_input = input("Enter a number (1-7): ")
        number = int(user_input)
        day = week(number)
        print(f"The day of the week is: {day}")
    except ValueError as e:
        print("Error:", e)
    except Exception:
        print("Error: Invalid input. Please enter a number between 1 and 7.")

main()