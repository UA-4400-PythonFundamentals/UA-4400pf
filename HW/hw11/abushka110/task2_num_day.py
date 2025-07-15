days_of_week = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

user_input = input("Enter a number from 1 to 7 to get the corresponding day of the week: ")

try:
    day_num = int(user_input)

    if day_num in (1,2,3,4,5,6,7):
        print(f"Your day is {days_of_week(day_num)}")
    else:
        raise ValueError("wrong number")
    
except ValueError as e:
    if str(e) == "wrong number":
        print("Wrong number. Please enter a number from 1 to 7.")
    else:
        print("You entered invalid data. Please enter a number from 1 to 7.")