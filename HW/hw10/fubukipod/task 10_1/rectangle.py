from typing import List, Union

Number = Union[int, float]

class Polygon:
    
    def __init__(self, sides: List[Number]):
        if len(sides) < 3:
            raise ValueError("Багатокутник має мати не менше ніж 3 сторони.")
        if not all(isinstance(s, (int, float)) and s > 0 for s in sides):
            raise ValueError("Всі сторони мають бути позитивними числами.")
        self._sides = sides.copy()

    @property
    def sides(self) -> List[Number]:
        return self._sides.copy()

    @property
    def perimeter(self) -> Number:
        return sum(self._sides)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(sides={self._sides})"


class Rectangle(Polygon):
    
    def __init__(self, width: Number, height: Number):
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Ширина та висота мають бути числами.")
        if width <= 0 or height <= 0:
            raise ValueError("Ширина та висота мають бути додатніми.")
        super().__init__([width, height, width, height])
        self.width = width
        self.height = height

    @property
    def area(self) -> Number:
        return self.width * self.height

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(width={self.width}, height={self.height})"