class Employee:
    """Class for representing name and salary of employees"""
    
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def display_total(cls):
        print(f"Total number of employees: {cls.count}")
employee1 = Employee("John", 1000)
employee2 = Employee("Jack", 2000)
employee1.display_info()
employee2.display_info()
Employee.display_total()
print("Base class:", Employee.__base__)
print("Class namespace (attributes):", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Class documentation:", Employee.__doc__)