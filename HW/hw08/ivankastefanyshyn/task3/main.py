import areas


def main():
    shape_name = input("Please enter the name of the shape:")

    if shape_name == "rectangle":
        length = float(input("Please enter the length of the rectangle"))
        width = float(input("Please enter the width of the rectangle"))
        print(f"The area of the rectangle is: {areas.rectangle_area(length, width)}")
    elif shape_name == "triangle":
        base = float(input("Please enter the base of the triangle"))
        height = float(input("Please enter the height of the triangle"))
        print(f"The area of the triangle is: {areas.triangle_area(base, height)}")
    elif shape_name == "circle":
        radius = float(input("Please enter the radius of the circle"))
        print(f"The area of the circle is: {areas.circle_area(radius)}")
    else:
        print("We don't have this shape")


if __name__ == "__main__":
    main()
