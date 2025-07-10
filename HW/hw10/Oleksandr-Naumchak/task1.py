# Task1. Create a polygon class and a rectangle class that inherits from the polygon class
# and finds the square of rectangle.

class Polygon:
    def __init__(self, count_of_sides):
        self.count_of_sides = count_of_sides

class Rectangle(Polygon):
    def __init__(self, width, length):
        super().__init__(4)
        self.width = width
        self.length = length

    def area(self):
        return self.length * self.width

r = Rectangle(7, 5)
print("Area of rectangle:", r.area())