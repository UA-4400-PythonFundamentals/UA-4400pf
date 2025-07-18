def get_weekday():
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    try:
        user_input = input("Enter a number from 1 to 7: ")
        num = int(user_input)

        if 1 <= num <= 7:
            return f"Day of the week: {days[num]}"
        else:
            return "There is no such day of the week (must be 1 to 7)."

    except ValueError:
        return "Invalid input. Please enter a number."

print(get_weekday())
