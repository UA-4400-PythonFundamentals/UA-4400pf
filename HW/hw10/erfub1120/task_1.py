class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def __str__(self):
        return f'Polygon with {self.sides} sides'
    
class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
width = int(input("Enter rectangle's width: "))
height = int(input("Enter rectangle's height: "))

rectangle = Rectangle(width, height)
print(f"Rectangle's area: {rectangle.area()}")
