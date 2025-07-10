class Employee:
    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1

    def get_total_employees(self):
        return Employee.counter

    def display_info(self):
        print(f"Employee: {self.name}, Salary: ${self.salary}")


emp1 = Employee("John", 50000)
emp2 = Employee("Alice", 60000)
emp3 = Employee("Bob", 55000)

emp1.display_info()
emp2.display_info()
emp3.display_info()

print(f"Total employees: {emp1.get_total_employees()}")

print(f"Base classes: {Employee.__bases__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation: {Employee.__doc__}")