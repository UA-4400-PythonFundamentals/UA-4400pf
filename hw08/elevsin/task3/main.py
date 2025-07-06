from areaFunctions import *

def calculate_area():
    try:
        polygon = int(input("Choose polygon:\n 1 - triangle\n 2 - rectangle\n 3 - circle\n input: "))
    except ValueError:
        print("You must enter a number.")
        return

    if polygon == 1:
        a = int(input("input base: "))
        h = int(input("input height: "))
        print(area_triangle(a, h))
    elif polygon == 2:
        a = int(input("input side: "))
        print(area_rectangle(a))
    elif polygon == 3:
        r = int(input("input radius: "))
        print(area_circle(r))
    else:
        print("Wrong answer")

calculate_area()