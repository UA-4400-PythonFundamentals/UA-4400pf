#2. Write a program that analyzes the entered number and, 
# depending on the number, gives the day of the week that corresponds to this number 
# (1 is Monday, 2 is Tuesday, etc.).
# Take into account cases of entering numbers from 8 and more, 
# as well as cases of entering non-numerical data.

def day_of_week():
    try:
        number = input("Enter a number >>> ")
        number = int(number)

    except ValueError:
        raise ValueError(f"Error: input must be numeric! Your input >>> {number} ")
    
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    if number < 1:
        raise ValueError(f"Error: input must be positive! Your input >>> {number} ")
    elif number > 7:
        raise ValueError(f"Error: input must be between 1 and 7! Your input >>> {number} ")
    else:
        print(f"Number {number} corresponds to {days[number]}")
        return days[number]

def main():
    try:
        day_of_week()
    except ValueError as ve:
        print(ve)
if __name__ == "__main__":
    main()