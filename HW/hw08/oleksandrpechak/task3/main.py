from areas import *

figure = str(int(input("Choose a figure: 1 - rectangle; 2 - triangle; 3 - circle: ")))
if figure == "1":
    print(area_of_rectangle(int(input("Width: ")), int(input("Height: "))))
elif figure == "2":
    print(area_of_triangle(int(input("Base: ")), int(input("Height: "))))
elif figure == "3":
    print(area_of_circle(int(input("Radius: "))))
else:
    print("There is no such figure. Try again.")
