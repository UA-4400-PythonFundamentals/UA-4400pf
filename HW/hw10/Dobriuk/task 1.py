class Polygon:
    def __init__(self, sides: int):
        if sides < 3:
            raise ValueError("A polygon must have at least 3 sides")
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, width: float, height: float):
        super().__init__(4)
        self.width = width
        self.height = height 
    def area(self) -> float:
        return self.width * self.height
    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})" 