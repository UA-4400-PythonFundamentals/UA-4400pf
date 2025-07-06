# print(type(list), list)
# inst = list()
# print(type(inst), inst)


# class Point:
#     pass

# print(type(Point), Point)
# point = Point()
# print(type(point), point)


# class Point:
#     x = 0
#     y = 0
#     def print(self):
#         print("Point_print")

# print(Point.x, Point.y )
# print(Point.print)
# class Point:
#     """A class representing a point in 2D space."""
#     count = 0

#     def __init__(self, x=0, y=0):
#         """Initialize a Point with x and y coordinates."""
#         print(f"Point.__init__ {x} {y}")
#         self.x = x
#         self.y = y
#         Point.count += 1

#     def print(self):
#         """Print the coordinates of the point."""
#         print(id(self))
#         print(f"Point_print {self.x} {self.y}")

# p1 = Point(1, 2)
# p2 = Point(3, 4)
# # print(f"p1: {p1.x}, {p1.y} {p1.count}")
# # print(f"p2: {p2.x}, {p2.y} {p2.count}")
# # p3 = Point(5, 6)

# # print(f"p1: {p1.x}, {p1.y} {p1.count}")
# # print(f"p2: {p2.x}, {p2.y} {p2.count}")
# # print(f"p3: {p3.x}, {p3.y} {p3.count}")
# # print(dir(p1))
# # print(p1.__dict__)
# # print(Point.__dict__)
# print(id(p1))
# p1.print()
# print(id(p2))
# p2.print()
# print(p1.__dict__)
# print(Point.__dict__)


# Point.print(p1)

# def print_point(p):
#     """Print the coordinates of a point."""
#     print(f"Point_print<{id(p)}> x:{p.x} y:{p.y}")

# print_point(p1)
# Point.my_print = print_point
# p1.my_print()

# f = Point.print
# f(p1)


# class Point:
#     """A class representing a point in 2D space."""

#     def __init__(self, x=0, y=0):
#         """Initialize a Point with x and y coordinates."""
#         self.x = x
#         self.y = y
#     def __del__(self):
#         """Destructor to clean up resources."""
#         print(f"Point.__del__ {self.x} {self.y}")


# def  f():
#     """Function to create and delete a Point."""
#     p = Point(1, 2)
#     print(f"Created Point: {p.x}, {p.y}")
# print("Before calling f()")
# f()
# print("After calling f()")
# print("Before calling f()")
# f()
# print("After calling f()")


# p1 = Point(1, 2)
# del p1
# p2 = Point(3, 4)

# print("End of program")


class Point:
    """A class representing a point in 2D space."""

    def __init__(self, x=0, y=0):
        """Initialize a Point with x and y coordinates."""
        self.x = x
        self.y = y

    # def __del__(self):
    #     """Destructor to clean up resources."""
    #     print(f"Point.__del__ {self.x} {self.y}")

    def __str__(self):
        """Return a detailed string representation of the Point."""
        return f"Point({self.x}, {self.y})"
    def __repr__(self):
        """Return a string representation of the Point."""
        return f"({self.x}, {self.y})"
    def __add__(self, other):
        """Add two Points together."""
        return Point(self.x + other.x, self.y + other.y)
    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def update(self, other):
        """Update the current Point with another Point's coordinates."""
        self.x += other.x
        self.y += other.y
        return self
    def __eq__(self, value):
        """Check if two Points are equal."""
        return self.x == value.x and self.y == value.y
    
p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1)  # Calls __str__
print(p2)  # Calls __str__
print([p1, p2])

p3 = p1+p2
p4 = p1.add(p2)
print(p3)  # Calls __str__
print(p1 == p2)  # Calls __eq__
print(p1 == Point(1, 2))  # Calls __eq__
print(p4)

p4.update(p1)
print(p4)  # Calls __str__