def rectangle_area(length,width):
    area = length * width
    return area
def triangle_area(base,height):
    area = (base * height) / 2
    return area
def circle_area(radius):
    pi = 3.14
    area = pi*radius**2
    return area
    
while True:
    print("Choose what area do you want to calculate: \n1. Rectangle \n2. Triangle \n3. Circle \nYour option (1,2,3): ")
    option = int(input())

    if option == 1:
        r_length = int(input("Provide length of rectangle(int): "))
        r_width = int(input("Provide width of rectangle(int): "))
        print(f"\nArea of rectangle is {rectangle_area(r_length,r_width)}\n")
    elif option == 2:
        t_base = int(input("Provide base of triangle(int): "))
        t_height = int(input("Provide height of triangle(int): "))
        print(f"\nArea of triangle is {triangle_area(t_base,t_height)}\n")
    elif option == 3:
        c_radius = int(input("Provide radius of circle(int): "))
        print(f"\nArea of circle is {circle_area(c_radius)}\n")
    else:
        print("There is no such an option! Choose between 1, 2 or 3.")
