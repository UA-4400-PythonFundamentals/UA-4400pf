from area_module import rectangle_area, triangle_area, circle_area

def main():
    print("Choose a figure to calculate area:")
    print("1 - Rectangle")
    print("2 - Triangle")
    print("3 - Circle")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        print("Rectangle area:", rectangle_area(a, b))

    elif choice == "2":
        h = float(input("Enter height h: "))
        a = float(input("Enter base a: "))
        print("Triangle area:", triangle_area(h, a))

    elif choice == "3":
        r = float(input("Enter radius r: "))
        print("Circle area:", circle_area(r))

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
