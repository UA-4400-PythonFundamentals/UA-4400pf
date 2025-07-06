# Task1
class Polygon:
    def __init__(self):
        pass
    
class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
# Task2

class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Hello {self.name}"
    
    @classmethod
    def species(cls):
        return 'Homosapiens'
    
    @staticmethod
    def species_static():
        return "Hello Homosapiens"

# Task3

class Employee:
    count = 0
    def __init__(self, name, salary):
        Employee.count += 1
        
        self.name = name
        self.salary = salary
        
    @classmethod
    def print_total_num_of_employs(cls):
        return f'Total number of employs : {cls.count}'

    def display_all_info(self):
        return f"Employ: {self.name}, salary: {self.salary}"

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)