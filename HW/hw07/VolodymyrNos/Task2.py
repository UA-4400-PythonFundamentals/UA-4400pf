def rectangle_area():
    """
    Calculates the area of a rectangle based on user input.

    Prompts the user to enter the width and length of the rectangle,
    converts them to integers, and returns the computed area.

    Returns:
        int: The area of the rectangle.
    """
    width = input("Enter a width of the rectangle: ")
    length = input("Enter a length of the rectangle: ")
    area = int(width) * int(length)
    return area
def triangle_area():
    """
    Calculates the area of a triangle based on user input.

    Prompts the user to enter the length of a triangle side and its height,
    converts them to integers, and returns the computed area using the formula:
    area = (base * height) / 2

    Returns:
        float: The area of the triangle.
    """
    side = input("Enter a lenght of triangle side: ")
    height = input("Enter a height of triangle: ")
    area = int(side)*int(height)*0.5
    return area
def circle_area():
    """
    Calculates the area of a circle based on user input.

    Prompts the user to enter the radius of the circle,
    converts it to an integer, and returns the computed area using the formula:
    area = π * r² (π ≈ 3.14)

    Returns:
        float: The area of the circle.
    """
    radius = input("Enter a radius of circle: ")
    area = 3.14*(int(radius)**2)
    return area
def area_calculate():
    """
    Asks the user to select a geometric figure and calculates its area.

    Prompts the user to choose between 'rectangle', 'triangle', or 'circle',
    then calls the corresponding function to compute the area.

    Returns:
        float or int: The calculated area of the selected figure.
        None: If the entered figure name is invalid.
    """
    figure = input("Enter a name of figure(rectangle, triangle, circle): ")
    if figure == "rectangle":
        return rectangle_area()
    elif figure == "triangle":
        return triangle_area()
    elif figure == "circle":
        return circle_area()
    else:
        print("There no such figure!")

area_calculate()