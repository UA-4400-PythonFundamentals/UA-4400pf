from math_module import rectangle_area, triangle_area, circle_area

def main():
    print("Choose the figure to calculate area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    choice = input("Enter 1, 2, or 3: ")

    if choice == '1':
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))
        print("Area of rectangle:", rectangle_area(a, b))
    elif choice == '2':
        a = float(input("Enter the base of the triangle: "))
        h = float(input("Enter the height of the triangle: "))
        print("Area of triangle:", triangle_area(a, h))
    elif choice == '3':
        r = float(input("Enter the radius of the circle: "))
        print("Area of circle:", circle_area(r))
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()