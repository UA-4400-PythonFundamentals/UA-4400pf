import math
from math import pi, pow
import area_module

def main():
    print("Choose a shape:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")
    choice = input("Enter your choice (1-3): ").strip()

    if choice == "1":
        a = float(input("Enter the length of the first side: "))
        b = float(input("Enter the length of the second side: "))
        area = area_module.rectangle_area(a, b)
        print("The area of the rectangle is:", area)
    elif choice == "2":
        r = float(input("Enter the radius of the circle: "))
        area = area_module.circle_area(r)
        print("The area of the circle is:", area)
    elif choice == "3":
        a = float(input("Enter the base of the triangle: "))
        h = float(input("Enter the height of the triangle: "))
        area = area_module.triangle_area(a, h)
        print("The area of the triangle is:", area)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()