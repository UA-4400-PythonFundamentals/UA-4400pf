from math import sqrt

def areaOfCircle(r):
    '''returns the area of a circle'''
    return 3.14 * r * r


def areaOfRectangle(w, h):
    '''returns the area of a rectangle'''
    return w * h


def areaOfTriangle(a, b, c):
    '''returns the area of a triangle'''
    halfPerimeter = (a + b + c) / 2
    return sqrt(halfPerimeter * (halfPerimeter - a) * (halfPerimeter - b) * (halfPerimeter - c))


shape = int(input("Enter the shape: \n 1 - Circle \n 2 - Rectangle \n 3 - Triangle"))
if (shape == 1):
    radius = float(input("Enter the radius: "))
    print("Area of a circle is equal", areaOfCircle(radius))
elif (shape == 2):
    width = float(input("Enter the width: "))
    height = float(input("Enter the height: "))
    print("Area of a rectangle is equal", areaOfRectangle(width, height))
elif (shape == 3):
    side1 = float(input("Enter the side1: "))
    side2 = float(input("Enter the side2: "))
    side3 = float(input("Enter the side3: "))
    print("Area of a triangle is equal", areaOfTriangle(side1, side2, side3))
else:
    print("Invalid input")