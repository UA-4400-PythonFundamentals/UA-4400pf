class Polygon:
    def __init__(self, sides):
        self.sides = sides
class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__([width, height, width, height])
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height
r = Rectangle(12, 14)
print("Площа прямокутника:", r.square())