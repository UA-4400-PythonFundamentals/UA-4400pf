import math

def max_of_two(a, b):
    
    return a if a > b else b

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def area_circle(radius):
    return math.pi * radius ** 2

def char_count(s):
    result = {}
    for char in s:
        result[char] = result.get(char, 0) + 1
    return result

def task1():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print("The larger number is:", max_of_two(a, b))

def task2():
    print("Calculate the area of a shape:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    choice = input("Choose a shape (1/2/3): ")

    if choice == "1":
        length = float(input("Enter the rectangle length: "))
        width = float(input("Enter the rectangle width: "))
        print(f"Area of rectangle: {area_rectangle(length, width):.2f}")
    elif choice == "2":
        base = float(input("Enter the triangle base: "))
        height = float(input("Enter the triangle height: "))
        print(f"Area of triangle: {area_triangle(base, height):.2f}")
    elif choice == "3":
        radius = float(input("Enter the circle radius: "))
        print(f"Area of circle: {area_circle(radius):.2f}")
    else:
        print("Invalid choice!")

def task3():
    string_input = input("Enter a string: ")
    counts = char_count(string_input)
    print("Character counts in the string:")
    for char, count in counts.items():
        print(f"'{char}': {count}")

def main():
    while True:
        print("\nSelect a task to perform:")
        print("1 - Find the larger of two numbers")
        print("2 - Calculate area of a shape")
        print("3 - Count characters in a string")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            task1()
        elif choice == "2":
            task2()
        elif choice == "3":
            task3()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()



