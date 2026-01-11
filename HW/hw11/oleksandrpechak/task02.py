def number(day_of_the_week):
    if day_of_the_week is not str:
        raise ValueError("This is not a number. Try again")
    elif day_of_the_week > 7:
        raise ValueError("There is no such day of the week. Try again.")
    elif day_of_the_week == 1:
        print("Monday")
    elif day_of_the_week == 2:
        print("Tuesday")
    elif day_of_the_week == 3:
        print("Wednesday")
    elif day_of_the_week == 4:
        print("Thursday")
    elif day_of_the_week == 5:
        print("Friday")
    elif day_of_the_week == 6:
        print("Saturday")
    elif day_of_the_week == 7:
        print("Sunday")
    else:
        day_of_the_week <= 0
        raise ValueError("There is no such day. Try positive numbers.")
    
try:
    number(input("Day of the week ? "))
except ValueError as e:
    print(e)