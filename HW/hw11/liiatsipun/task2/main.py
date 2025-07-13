def main():
    number = input("Number ")
    if not all(char.isdigit() for char in number):
        raise ValueError("Enter the number from 1 to 7")
    process_day(number)


def process_day(number):
    if number < 1 or number > 7:
        raise ValueError("Enter the number from 1 to 7")
    if number == 1:
        print("Monday")
    elif number == 2:
        print("Tuesday")
    elif number == 3:
        print("Wednesday")
    elif number == 4:
        print("Thursday")
    elif number == 5:
        print("Friday")
    elif number == 6:
        print("Saturday")
    elif number == 7:
        print("Sunday")

main()
