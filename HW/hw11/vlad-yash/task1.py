#1. Write a program that prompts the user to enter their age,
# and then displays a message stating whether the age is even or odd.
# The program must provide the ability to enter a negative number,
# and in this case generate an exception. The master code should call a function 
# that processes the information entered.

def enter_age():

    try:
        age = int(input("Enter your age: "))
    except ValueError:
        raise ValueError("Error: Age must be a number")
    if age < 0:
        raise ValueError("Error: Age has a negative value")
    elif age % 2 == 0:
        print(f"Your age {age} - is even!")
    else:
        print(f"Your age {age} -  is odd!")
    

def main():
    try:
        enter_age()
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()
