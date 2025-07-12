def get_day_name(day_num):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return days.get(day_num, None)

def analyze_day_input(data):
    try:
        day = int(data)
        if day < 1 or day > 7:
            return "Number most be between 1 and 7."
    except ValueError:
        return "Invalid input. Please enter a number between 1 and 7."
    else:
        return f"{day} is {get_day_name(day)}."

user_input = input("Enter a number between 1 and 7: ")
print(analyze_day_input(user_input))