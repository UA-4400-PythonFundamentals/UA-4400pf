
'''Task 1. Create a polygon class and a rectangle class that inherits from the polygon class
 and finds the square of rectangle.'''

class Polygon:
    def __init__(self, side_1: int, side_2: int, side_n: int):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_n = side_n

class Rectangle(Polygon):
    def __init__(self, side_1, side_2):
        super().__init__(side_1, side_2)

    def rect_square(self):
        square = self.side_1 * self.side_2
        return square


'''Task 2. Create a class Human, everyone has a name, create a method in the class that displays 
a welcome message to each person. Create a class method in the class that returns information 
that it is a species of "Homosapiens". And in the class create a static method that returns an 
arbitrary message.'''

class Human:
    species = "no information"

    def __init__(self, name: str):
        self.name = name

    def hum_greeting(self):
        return f"Hello, {self.name}."

    @classmethod
    def hum_species(cls):
        cls.species = "Homosapiens"
        return f"You are {cls.species}."

    @staticmethod
    def message():
        return "Homo sapiens means 'wise human'."


'''Task 3. Create an employee class. Each employee has characteristics such as name and salary.
 The class should have a counter that calculates the total number of employees, as well as a 
 method that prints the total number of employees and a method that displays information about 
 each employee in particular, namely the name and salary. In addition to creating a class, 
 display information about the base classes from which the employee class is inherited (__base__),
 the class namespace (__dict__), the class name (__name__), the module name in which the class 
 is defined (__module__), the documentation bar (__doc__).'''

class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def total_emp(cls):
        print(cls.count)

    def display_info(self):
        print(f"Employee name: {self.name}, salary: {self.salary}")

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)