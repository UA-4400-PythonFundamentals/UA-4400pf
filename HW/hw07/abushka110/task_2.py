import math

def area_rectangle(length, width):
    """
    Calculates the area of a rectangle.

    Parameters:
    length (float): Rectangle length.
    width (float): Rectangle width.

    Returns:
    float: Rectangle area.
    """
    return length * width


def area_triangle(base, height):
    """
    Calculates the area of a triangle.

    Parameters:
    base (float): Triangle base.
    height (float): Triangle height.

    Returns:
    float: Triangle area.
    """
    return 0.5 * base * height


def area_circle(radius):
    """
    Calculates the area of a circle.

    Parameters:
    radius (float): Circle radius.

    Returns:
    float: Circle area.
    """
    return math.pi * radius ** 2


def get_float(prompt):
    """
    Prompts the user to enter a valid float.

    Parameters:
    prompt (str): Message to show the user.

    Returns:
    float: Valid float entered by the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")


def get_shape_choice():
    """
    Prompts the user to choose a valid shape option.

    Returns:
    str: One of the valid choices ("1", "2", or "3").
    """
    print("Choose a shape to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    while True:
        choice = input("Enter choice (1/2/3): ")
        if choice in ("1", "2", "3"):
            return choice
        else:
            print("Invalid input! Please enter 1, 2, or 3.")


def main():
    choice = get_shape_choice()

    if choice == "1":
        length = get_float("Enter length: ")
        width = get_float("Enter width: ")
        print("Area of rectangle:", area_rectangle(length, width))

    elif choice == "2":
        base = get_float("Enter base: ")
        height = get_float("Enter height: ")
        print("Area of triangle:", area_triangle(base, height))

    elif choice == "3":
        radius = get_float("Enter radius: ")
        print("Area of circle:", area_circle(radius))

if __name__ == "__main__":
    main()
