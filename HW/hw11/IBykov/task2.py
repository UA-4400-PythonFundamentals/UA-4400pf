def get_day(number):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if number < 1 or number > 7:
        if number >= 8:
            raise ValueError("Number is too big")
        else:
            raise ValueError("Number is too small")

    return days[number - 1]


try:
    num = int(input("Enter a number (1-7): "))
    day = get_day(num)
    print(f"Day {num} is {day}")
except ValueError as e:
    print(f"Error: {e}")
except:
    print("Error: Please enter a valid number")