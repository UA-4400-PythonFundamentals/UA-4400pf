from areas import rectangle_area, triangle_area, circle_area

def main():
    print("Choose the shape to calculate area:")
    print("1 - Rectangle")
    print("2 - Triangle")
    print("3 - Circle")
    choice = input("Enter 1, 2 or 3: ")

    if choice == "1":
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        print(f"Rectangle area = {rectangle_area(a, b):.2f}")

    elif choice == "2":
        a = float(input("Enter base a: "))
        h = float(input("Enter height h: "))
        print(f"Triangle area = {triangle_area(a, h):.2f}")

    elif choice == "3":
        r = float(input("Enter radius r: "))
        print(f"Circle area = {circle_area(r):.2f}")

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
