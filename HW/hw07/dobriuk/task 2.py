import math
def rectangle_area(width: float, height: float) -> float:
   """
   returm the area of the rectangle.
   paraparameter width of the rectangle
   parameter height of the rectangle
   """
   return width * height

def triangle_area(base: float, height: float) -> float:
    """
    return the area of the triangle.
    parameter base of the triangle
    parameter height of the triangle
    """
    return 0.5 * base * height

def circle_area(radius: float) -> float:
    """
    return the area of the circle.
    parameter radius of the circle
    """
    return math.pi * radius ** 2

def main():
    """
    Interactive menu to choose and calculate the area of different shapes.
    """
    print("Choose your task: \n"
        "rectangle_area = 1 \n", 
        "triangle_area = 2 \n", 
        "circle_area = 3", )
    choice = input("Enter your numbeer of the task: ").strip()
    if choice == "1":
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        print(f"The area of the rectangle is {rectangle_area(width, height)}")
    elif choice == "2":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        print(f"The area of the triangle is {triangle_area(base, height)}")
    elif choice == "3":
        radius = float(input("Enter radius: "))
        area = circle_area(radius)
        print(f"The area of the circle is {area}")
    else:
        print("Invalid choice")
if __name__ == "__main__":
    main()

