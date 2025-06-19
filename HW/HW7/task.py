import math
def task1(a, b):
    return a if a > b else b

def task2_rectangle(length, width):
    return length * width

def task2_triangle(base, height):
    return 0.5 * base * height

def task2_circle(radius):
    return math.pi * radius * radius

def task3(string):
    result = {}
    for char in string:
        result[char] = result.get(char, 0) + 1
    return result

print(task1(5, 10))

print("Area Calculator")
print("1. Rectangle")
print("2. Triangle")
print("3. Circle")
choice = input("Enter your choice (1/2/3): ")

if choice == '1':
    length = float(input("Enter length of rectangle: "))
    width = float(input("Enter width of rectangle: "))
    area = task2_rectangle(length, width)
    print(f"Area of rectangle: {area}")
elif choice == '2':
    base = float(input("Enter base of triangle: "))
    height = float(input("Enter height of triangle: "))
    area = task2_triangle(base, height)
    print(f"Area of triangle: {area}")
elif choice == '3':
    radius = float(input("Enter radius of circle: "))
    area = task2_circle(radius)
    print(f"Area of circle: {area}")
else:
    print("Invalid choice.")

print(task3("hello world"))