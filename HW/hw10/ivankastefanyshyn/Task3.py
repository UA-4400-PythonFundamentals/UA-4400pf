class Employee:
    """
    The Employee class stores information about an employee: name and salary.
    It also keeps track of the total number of employees created.
    """

    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def display_employee_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def display_employee_count(cls):
        print(f"The number of employees is: {cls.employee_count}")


employees = [
    Employee("Jane Doe", 1000),
    Employee("John Doe", 2000),
    Employee("James Doe", 3000),
    Employee("Juliya Doe", 4000),
]
for employee in employees:
    employee.display_employee_info()

Employee.display_employee_count()

print()
print("\tBase class:", Employee.__base__)
print("\tClass namespace:", Employee.__dict__)
print("\tClass name:", Employee.__name__)
print("\tModule name:", Employee.__module__)
print("\tDocumentation bar:", Employee.__doc__)
