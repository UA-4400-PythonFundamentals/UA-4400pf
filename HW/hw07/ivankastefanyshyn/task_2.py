def rectangle_area(length, width):
    area = length * width
    return area


def triangle_area(base, height):
    area = base * height * 0.5
    return area


def circle_area(radius):
    PI = 3.14
    area = PI * radius**2
    return area


def main():
    shape_name = input("Please enter the name of the shape:")

    if shape_name == "rectangle":
        length = float(input("Please enter the length of the rectangle"))
        width = float(input("Please enter the width of the rectangle"))
        print(f"The area of the rectangle is: {rectangle_area(length, width)}")
    elif shape_name == "triangle":
        base = float(input("Please enter the base of the triangle"))
        height = float(input("Please enter the height of the triangle"))
        print(f"The area of the triangle is: {triangle_area(base, height)}")
    elif shape_name == "circle":
        radius = float(input("Please enter the radius of the circle"))
        print(f"The area of the circle is: {circle_area(radius)}")
    else:
        print("We don't have this shape")


main()
