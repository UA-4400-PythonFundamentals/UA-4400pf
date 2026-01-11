# Task3. Create an employee class. Each employee has characteristics such as name and salary. 
# The class should have a counter that calculates the total number of employees, as well as a method that prints the total number of employees and
#  a method that displays information about each employee in particular, namely the name and salary.
#  In addition to creating a class, display information about the base classes 
#  from which the employee class is inherited (__base_),
# the class namespace (__dict__), the class name (_name_), the module name in which the class is defined (module_), the documentation bar (_doc_)

class Person:
    """Base class representing a person."""
    pass
class Employee(Person):
    ''' This is doc.'''
    count = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def total(self):
        print(f"Total number of employee : {Employee.count}")
    
    def characteristics(self):
        print(f"Name : {self.name}, Salary : {self.salary}" )
        pass

    
    def info(self):
        self.characteristics()
        pass

print("Base class:", Employee.__base__)
print("Space of class names:", Employee.__dict__)
print("Name of the class:", Employee.__name__)
print("Moduleс:", Employee.__module__)
print("Documentation:", Employee.__doc__)

emp1 = Employee("Olena", 1000)
emp2 = Employee("Ivan", 1200)

emp1.info()
emp2.info()
emp1.total()