class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def display_employee(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def display_count(cls):
        print(f"Total Employees: {cls.total_employees}")

if __name__ == "__main__":
    emp1 = Employee("Alice", 50000)
    emp2 = Employee("Bob", 60000)
    emp1.display_employee()
    emp2.display_employee()
    Employee.display_count()

    print("\nClass Introspection:")
    print("Base classes:", Employee.__bases__)
    print("Class namespace:", Employee.__dict__)
    print("Class name:", Employee.__name__)
    print("Module name:", Employee.__module__)
    print("Documentation:", Employee.__doc__)