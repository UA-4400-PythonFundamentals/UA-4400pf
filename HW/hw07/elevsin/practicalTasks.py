# Task1
def largest_number(a, b):
    """ Returns the largest of two numbers. """
    return a if a > b else b

largest_number(4, 7)

#Task2
import math
def area_triangle(a, h):
    return (1/2) * a * h

def area_rectangle(a):
    return a * a

def area_circle(r):
    return math.pi * r * r

def calculate_area():
    polygon = int(input("Choose polygon:\n 1 - triangle\n 2 - rectangle\n 3 - circle\n"))
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

#Task3
def numb_of_char(text):
    return {i + 1: char for i, char in enumerate(text)}

print(numb_of_char("text"))