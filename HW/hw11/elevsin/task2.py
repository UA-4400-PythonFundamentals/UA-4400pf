import calendar

def get_weekday(num):
    try:
        num = int(num)
    except ValueError:
        raise ValueError("Invalid input: please enter a number from 1 to 7")
    if num < 1 or num > 7:
        raise ValueError("Error: number must be between 1 and 7")
    return calendar.day_name[num - 1]

def main():
    user_input = input("Enter a number for the day of the week: ")
    try:
        day = get_weekday(user_input)
    except ValueError as e:
        print(e)
    else:
        print(f"The day is: {day}")

main()
