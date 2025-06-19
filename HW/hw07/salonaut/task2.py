def rectangle_area(width, height):
    return width * height

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    P = 3.14
    return P * radius ** 2


def main():
    print('1 - Calculate area of Rectangle \n2 - Calculate area of Triangle \n3 - Calculate area of Circle \n4 - Exit')
    while True:
        user_choice = int(input('Enter choice: '))
        if user_choice == 1:
            a = int(input('Enter width: '))
            b = int(input('Enter height: '))
            print(rectangle_area(a, b))
        elif user_choice == 2:
            a = int(input('Enter base: '))
            h = int(input('Enter height: '))
            print(triangle_area(a, h))
        elif user_choice == 3:
            r = int(input('Enter Radius: '))
            print(circle_area(r))
        elif user_choice == 4:
            break
        else:
            print('Invalid input. ')

if __name__ == "__main__":
    main()