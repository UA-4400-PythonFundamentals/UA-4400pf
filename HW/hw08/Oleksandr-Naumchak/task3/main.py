from calculation import *

def main():
    print("Choose a figure to calculate area:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        a = float(input("Enter side length: "))
        b = float(input("Enter side width: "))
        print(f"Rectangle area = {rectangle_area(a, b)}")
    
    elif choice == "2":
        r = float(input("Enter radius r: "))
        print(f"Circle area = {circle_area(r)}")

    elif choice == "3":
        a = float(input("Enter base a: "))
        h = float(input("Enter height h: "))
        print(f"Triangle area = {triangle_area(a, h)}")

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()