from math import pi, pow

def rect_area(a, b):
    """Calculate the area of a rectangle."""
    return a * b

def circle_area(r):
    """Calculate the area of a circle."""
    return pi * pow(r, 2)

def triangle_area(a, h):
    """Calculate the area of a triangle."""
    return 0.5 * a * h