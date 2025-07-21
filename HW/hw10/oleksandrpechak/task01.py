# Task1. Create a polygon class and a rectangle class that inherits from the polygon class and finds the square of rectangle. 
class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4)
        self.length = length
        self.width = width
    def area(self):
        return self.width*self.length

a = Rectangle(12,12)
print(a.area())