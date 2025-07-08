import math
from math import pow, pi

import myModule

figure = input("Enter one of follows figures the area of which you want to calculate: circle/rectangle/triangle/.\n")
if figure == "circle":
    r = int(input("Enter the radius: "))
    print(myModule.circle_area(pi, r))
if figure == "rectangle":
    a = int(input("Enter the length: "))
    b = int(input("Enter the width: "))
    print(myModule.rectangle_area(a, b))
if figure == "triangle":
    h = int(input("Enter the height: "))
    a = int(input("Enter the base: "))
    print(myModule.triangle_area(h, a))

