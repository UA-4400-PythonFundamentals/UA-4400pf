'''1. Write a program that prompts the user to enter their age, and then displays a message
 stating whether the age is even or odd. The program must provide the ability to enter a 
 negative number, and in this case generate an exception. The master code should call a function
  that processes the information entered.'''

class MyError(Exception):
    pass

def check_positive(age):
    if age < 0:
        raise MyError("You entered a negative number, that couldn`t be an age.")
    return age

def check_odd_even(age):
    try:
        age = int(age)
        check_positive(age)
        if age % 2 == 0:
            return "Your age is even"
        else:
            return "Your age is odd"
    except MyError as e:
        return e

age = input("Enter your age: ")
print(check_odd_even(age))



'''2. Write a program that analyzes the entered number and, depending on the number, gives 
the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.). Take 
into account cases of entering numbers from 8 and more, as well as cases of entering 
non-numerical data.'''

class MyError(Exception):
    pass

def number_check(number):
    if not (1 <= number <= 7):
        raise MyError("Wrong number. Must be from 1 to 7")
    return number

def day_of_week(number):
    try:
        if number_check(number):
            week = {
                    1: "Monday",
                    2: "Tuesday",
                    3: "Wednesday",
                    4: "Thursday",
                    5: "Friday",
                    6: "Saturday",
                    7: "Sunday"}
            return week.get(number)
    except MyError as e:
        return e

try:
    number = int(input("Enter a number from 1 to 7: "))
    print(day_of_week(number))
except ValueError:
    print("Not a number. Must be number from 1 to 7")
