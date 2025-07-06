import math
from Calculations import calculate_area, calculate_area_rectangle, calculate_area_triangle

a = input("Area of which figure you want to calculate? (circle, rectangle, triangle): ").strip().lower()
if a == "circle":
    r = float(input("Enter the radius of the circle: "))
    print(f"The area of circle is: {calculate_area(r)}")
elif a == "rectangle":
    l = float(input("Enter length of the rectangle: "))
    w = float(input("Enter width of the rectangle: "))
    print(f"The area of the rectangle is: {calculate_area_rectangle(l, w)}")
elif a == "triangle":
    b = float(input("Enter base of the triangle: "))
    h = float(input("Enter height of the triangle: "))
    print(f"The area of triangle is: {calculate_area_triangle(b, h)}")
else:
    print("Unknown figure.")