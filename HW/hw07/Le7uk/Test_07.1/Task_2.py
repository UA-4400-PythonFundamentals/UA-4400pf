def area_of_rectangle(length: float, width: float) :
    """
    Обчислює площу прямокутника.

    Аргументи:
    length -- довжина прямокутника
    width -- ширина прямокутника

    Повертає:
    float -- площа прямокутника
    """
    return length * width
def area_of_square(side: float) :
    """
    Обчислює площу квадрата.

    Аргументи:
    side -- довжина сторони квадрата

    Повертає:
    float -- площа квадрата
    """
    return side ** 2
def area_of_circle(radius: float) :
    """
    Обчислює площу круга.

    Аргументи:
    radius -- радіус круга

    Повертає:
    float -- площа круга
    """
    
    return 3.14 * radius ** 2

a = input("Enter area you want to calculate (rectangle, square, circle): ").strip().lower()
if a == "rectangle":
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area of rectangle:", area_of_rectangle(l, w))
elif a == "square":
    s = float(input("Enter side length: "))
    print("Area of square:", area_of_square(s))
elif a == "circle":
    r = float(input("Enter radius: "))
    print("Area of circle:", area_of_circle(r))
else:
    print("Invalid input.")