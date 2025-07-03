#Task2. Write a program that calculates the area of a rectangle, triangle and circle
#(write three functions to calculate the area.
# And call them in the main program depending on the user's choice).

from math import pi

#area of a rectangle
def rectangle_area(length, width):
    return length * width


#area of a triangle
def triangle_area(base, height):
    return 0.5 * base * height


#area of a circle
def circle_area(radius):
    return pi * radius ** 2


# get and check if input is a number 
def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            if number <= 0:
                print("The number must be positive")
            else:
                return number
        except ValueError:
            print("Input must be a number")

def main():
    print("Let's calculate the area")
    print("Choose the shape:")
    print("\t 1  :rectangle")
    print("\t 2  :triangle")
    print("\t 3  :circle")

    shape = input("Enter 1, 2 or 3:  ")

    if shape == "1":
        length = get_number("Enter the length:  ")
        width = get_number("Enter the width:  ")
        print(f"Area of the rectangle is {round(rectangle_area(length, width), 2)}")

    elif shape == "2":
        base = get_number("Enter the base:  ")
        height = get_number("Enter the height:  ")
        print(f"Area of the triangle is {round(triangle_area(base, height), 2)}")

    elif shape == "3":
        radius = get_number("Enter the radius:  ")
        print(f"Area of the circle is {round(circle_area(radius), 2)}")
        
    else:
        print("Incorrect choice!")

if __name__ == "__main__":
    main()