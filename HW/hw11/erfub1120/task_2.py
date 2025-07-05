while True:
    try:
        user_input = input("Enter a number between 1 and 7: ")

        number = int(user_input)

        if number < 1 or number > 7:
            raise ValueError("There are only 7 days in a week. Please enter a number between 1 and 7.")

    except ValueError as e:
        if "invalid literal" in str(e):
            print("Please provide an integer number.")
        else:
            print(e)
    else:
        if number == 1:
            print("1 is Monday")
        elif number == 2:
            print("2 is Tuesday")
        elif number == 3:
            print("3 is Wednesday")
        elif number == 4:
            print("4 is Thursday")
        elif number == 5:
            print("5 is Friday")
        elif number == 6:
            print("6 is Saturday")
        elif number == 7:
            print("7 is Sunday")