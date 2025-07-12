def day_of_the_week(day):
    if day == 1:
        print("It's Monday")
    elif day == 2:
        print("It's Tuesday")
    elif day == 3:
        print("It's Wednesday")
    elif day == 4:
        print("It's Thursday")
    elif day == 5:
        print("It's Friday")
    elif day == 6:
        print("It's Saturday")
    elif day == 7:
        print("It's Sunday")
    else:
        raise ValueError("Number out of range. Please enter numbers between 1 and 7")


user_input = input("Please enter the number of the day in the week:")

try:
    day = int(user_input)
except ValueError:
    print("Error: You entered non-numerical data.Please enter numbers between 1 and 7")
else:
    try:
        day_of_the_week(day)
    except ValueError as m:
        print("Error:", m)
