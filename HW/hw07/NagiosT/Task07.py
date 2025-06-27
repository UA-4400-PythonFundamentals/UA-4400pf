#Task1
#Function that returns largest number
def get_largest(a, b): 
    if a > b: 
	return a
    else:
        return b


#Task2
import math

#calculate the area of a rectangle
def area_rectangle(length, width):
    return length * width

#calculate the area of a triangle
def area_triangle(base, height):
    return 0.5 * base * height

#calculate the area of a circle
def area_circle(radius):
    return math.pi * radius ** 2

#program
def main():
    print("Choose a shape to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = input("Enter 1, 2, or 3: ")

    if choice == '1':
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = area_rectangle(length, width)
        print(f"Area of rectangle: {area:.2f}")

    elif choice == '2':
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        area = area_triangle(base, height)
        print(f"Area of triangle: {area:.2f}")

    elif choice == '3':
        radius = float(input("Enter the radius: "))
        area = area_circle(radius)
        print(f"Area of circle: {area:.2f}")

    else:
        print("Invalid choice!")

main()


#task3
def count_characters(text):
    result = {}
    for char in text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result
