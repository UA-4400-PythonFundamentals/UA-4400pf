class Polygon():
    def __init__(self, *sides):
        self.sides = sides

    def area(self):
        print('Not implemented!')


class Rectangle(Polygon):
    def __init__(self, *sides):
        super().__init__(*sides)

    def area(self):
        return self.sides[0] * self.sides[1]


rect = Rectangle(3, 5)
print(rect.area())
