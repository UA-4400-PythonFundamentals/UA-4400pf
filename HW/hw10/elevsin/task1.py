class Polygon:
    def __init__(self, width):
        self.width = width

    def area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(width)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(4, 5)
print("Площа:", rect.area())