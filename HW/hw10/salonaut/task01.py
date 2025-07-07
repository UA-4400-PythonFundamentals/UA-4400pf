class Polygon:
    def __init__(self, num_sides: int):
        self.sides = num_sides


    def __str__(self):
        return f'Polygon with {self.sides} sides'



class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(4)
        self.width = width
        self.height = height



    def calculate_area(self):
        return self.width * self.height


    def __str__(self):
        return f'Rectangle with width {self.width} and height {self.height}'
