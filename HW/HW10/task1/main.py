class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.sides = [0 for _ in range(num_sides)]

    def input_sides(self, sides):
        if len(sides) != self.num_sides:
            raise ValueError("Incorrect number of sides.")
        self.sides = sides

    def display_sides(self):
        for i, length in enumerate(self.sides):
            print(f"Side {i+1} is {length}")

class Rectangle(Polygon):
    def __init__(self, length=0, width=0):
        super().__init__(4)
        self.length = length
        self.width = width
        self.sides = [length, width, length, width]

    def set_dimensions(self, length, width):
        self.length = length
        self.width = width
        self.sides = [length, width, length, width]

    def area(self):
        return self.length * self.width

if __name__ == "__main__":
    rect = Rectangle()
    rect.set_dimensions(5, 3)
    print("Rectangle sides:")
    rect.display_sides()
    print("Area of rectangle:", rect.area())