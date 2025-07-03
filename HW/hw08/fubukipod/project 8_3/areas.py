import math
from math import pow, pi

def area_rectangle(a: float, b: float) -> float:
    return a * b


def area_triangle(height: float, base: float) -> float:
    return 0.5 * height * base


def area_circle(radius: float) -> float:
    return pi * pow(radius, 2)