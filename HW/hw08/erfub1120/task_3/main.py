from areas import *

def main():
    while True:
        print("Choose an option:")
        print("1. Calculate area of a circle")
        print("2. Calculate area of a rectangle")
        print("3. Calculate area of a triangle")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            r = float(input("Enter the radius of the circle: "))
            area = circle_area(r)
            print(f"The area of the circle is: {area}")
        elif choice == '2':
            a = float(input("Enter the length of the rectangle: "))
            b = float(input("Enter the width of the rectangle: "))
            area = rect_area(a, b)
            print(f"The area of the rectangle is: {area}")
        elif choice == '3':
            a = float(input("Enter the base of the triangle: "))
            h = float(input("Enter the height of the triangle: "))
            area = triangle_area(a, h)
            print(f"The area of the triangle is: {area}")
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
            
main()