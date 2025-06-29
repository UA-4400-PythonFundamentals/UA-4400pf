from math import pow, pi


def rectangle_area(length, width):
    area = length * width
    return area


def triangle_area(base, height):
    area = base * height * 0.5
    return area


def circle_area(radius):
    area = pi * pow(radius, 2)
    return area
