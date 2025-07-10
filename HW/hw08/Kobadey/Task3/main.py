from areas import *

shape = int(input("Enter the shape: \n 1 - Circle \n 2 - Rectangle \n 3 - Triangle"))
if (shape == 1):
    radius = float(input("Enter the radius: "))
    print("Area of a circle is equal", areaOfCircle(radius))
elif (shape == 2):
    width = float(input("Enter the width: "))
    height = float(input("Enter the height: "))
    print("Area of a rectangle is equal", areaOfRectangle(width, height))
elif (shape == 3):
    side = float(input("Enter the side: "))
    height = float(input("Enter the height: "))
    print("Area of a triangle is equal", areaOfTriangle(side, height))
else:
    print("Invalid input")