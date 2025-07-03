class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def __str__(self):
        return f"Point({self.__x}, {self.__y})"
    def get_x(self):
        print("Getting x")
        return self.__x
    def set_x(self, x):
        print("Setting x")
        if not isinstance(x, (int, float)):
            print("x must be a number")
            return
        self.__x = int(x)
    x = property(get_x, set_x)

    @property
    def y(self):
        print("Getting y")
        return self.__y
    @y.setter
    def y(self, y):
        print("Setting y")
        if not isinstance(y, (int, float)):
            print("y must be a number")
            return
        self.__y = int(y)
p = Point(1, 2)
print(p)  # Output: Point(1, 2)
# print(p._Point__x)  # Accessing the name-mangled attribute
# print(p.get_x())  # Output: Getting x\n1
# p.set_x(10)  # Output: Setting x
# print(p)  # Output: Point(10, 2)
# p.set_x("abc")  # Output: x must be a number
# print(p)  # Output: Point(10, 2)
p.x = 20  # Using the property setter
print(p.x)  # Output: Point(20, 2)
p.y = 30  # Using the property setter
print(p.y)  # Output: 30
print(p)  # Output: Point(20, 30)
    