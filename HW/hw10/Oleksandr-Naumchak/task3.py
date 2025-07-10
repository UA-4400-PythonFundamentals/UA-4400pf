#Task3. Create an employee class. Each employee has characteristics such as name and salary.
# The class should have a counter that calculates the total number of employees,
# as well as a method that prints the total number of employees
# and a method that displays information about each employee in particular,
# namely the name and salary. In addition to creating a class, display information about
# the base classes from which the employee class is inherited (__base__),
# the class namespace (__dict__), the class name (__name__), the module name in which
# the class is defined (__module__), the documentation bar (__doc__)

class Employee:
    """Employee class stores employee data and tracks the count of employees."""
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def total_employees(cls):
        print(f"Total employees: {cls.count}")

e1 = Employee("John", 5000)
e2 = Employee("Anna", 6000)

e1.display_info()
e2.display_info()
Employee.total_employees()

# Отображение метаинформации о классе:
print("Base class:", Employee.__base__)
print("Namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Docstring:", Employee.__doc__)
