# Task1. Create a polygon class and a rectangle class that inherits from the polygon class
# and finds the square of rectangle.

class Polygon:

    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides


class Rectangle(Polygon):

    def __init__(self, width, height):
        super().__init__(4)
        self.width = width
        self.height = height
    
    def square(self):
        return self.width * self.height
    
#x = Rectangle(5, 7)
#print(x.square())