import math

def area_of_rectangle(a, b):
    return a * b

def area_of_triangle(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s

def area_of_circle(r):
    return math.pi * math.pow(r, 2)
