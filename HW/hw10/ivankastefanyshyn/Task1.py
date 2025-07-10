class Polygon:
    def __init__(self):
        print("It's a polygon")


class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        area = self.width * self.height
        return area


rect = Rectangle(5, 10)
print(f"The area of rectangle is {rect.area()}")
