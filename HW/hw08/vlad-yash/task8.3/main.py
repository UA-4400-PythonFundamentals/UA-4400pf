import area

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
        result = area.rectangle_area(length, width)
        print(f"Area of the rectangle is {round(result, 2)}")

    elif shape == "2":
        base = get_number("Enter the base:  ")
        height = get_number("Enter the height:  ")
        result = area.triangle_area(base, height)
        print(f"Area of the triangle is {round(result, 2)}")

    elif shape == "3":
        radius = get_number("Enter the radius:  ")
        result = area.circle_area(radius)
        print(f"Area of the circle is {round(result,2)}")
    
    else:
        print("Incorrect choice!")

if __name__ == "__main__":
    main()