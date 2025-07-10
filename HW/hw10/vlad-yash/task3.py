#Task3. Create an employee class. Each employee has characteristics such as name and salary.
# The class should have a counter that calculates the total number of employees,
# as well as a method that prints the total number of employees
# and a method that displays information about each employee in particular,
# namely the name and salary. In addition to creating a class, display information about
# the base classes from which the employee class is inherited (__base__),
# the class namespace (__dict__), the class name (__name__), the module name in which
# the class is defined (__module__), the documentation bar (__doc__)

class Employee:
    """
    
    Task 3 solution.
    Class Employee representing an employee with a name and salary.
    """

    __counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.__counter += 1
    
    def info(self):
        print(f"Name: {self.name} >> salary: {self.salary}")

        

    @classmethod
    def total_number_of_employees(cls):
        print (f"Total number of employees: {cls.__counter}")

emp1 = Employee("John", 10000)
emp2 = Employee("Dou", 5000)

emp1.info()
emp2.info()

Employee.total_number_of_employees()

print("Base: ", Employee.__base__)
print("Namespace: ", Employee.__dict__)
print("Class name: ", Employee.__name__)
print("Module name: ", Employee.__module__)
print("DOCstring: ", Employee.__doc__)