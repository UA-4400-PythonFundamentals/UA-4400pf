class Polygon:
    def __init__(self, sides):
        self.sides = sides      # list of side lengths

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width])
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
if __name__ == "__main__":
    # Example usage
    rect = Rectangle(5, 3)
    print("Sides of rectangle:", rect.sides)
    print("Area of rectangle:", rect.area())