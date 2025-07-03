# Напиши програму, яка обчислює площу прямокутника, трикутника та кола.
# Створи три окремі функції для обчислення площі.
# У головній частині програми викликай відповідну функцію залежно від вибору користувача.
def area_of_rectangle (w, h):
    """
    Calculate the area of a rectangle
    """
    if w and h:
        return w*h
def area_of_triangle(b, h):
    """
    Calculate the area of a triangle
    """
    if b and h:
        return 1/2*b*h
def area_of_circle(r):
    """
    Calculate the are of a circle
    """
    if r:
        import math
        return math.pi*r**2

figure = str(int(input("Choose a figure: 1 - rectangle; 2 - triangle; 3 - circle: ")))
if figure == "1":
    print(area_of_rectangle(int(input("Width: ")), int(input("Height: "))))
elif figure == "2":
    print(area_of_triangle(int(input("Base: ")), int(input("Height: "))))
elif figure == "3":
    print(area_of_circle(int(input("Radius: "))))
else:
    print("There is no such figure. Try again.")



    