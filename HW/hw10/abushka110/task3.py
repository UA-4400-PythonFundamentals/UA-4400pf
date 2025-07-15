class Employee:
    number_of_employees = 0
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary
        Employee.number_of_employees += 1

    # method to show employee details
    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    # Class method to show total number of employees
    @classmethod
    def display_total_employees(cls):
        print(f"Total Employees: {cls.number_of_employees}")

if __name__ == "__main__":
    # Example usage
    e1 = Employee("John", 20000)
    e2 = Employee("Andriy", 3000)

    e1.display_info()
    e2.display_info()

    Employee.display_total_employees()

    # Display class metadata
    print("\n--- Class Metadata ---")
    print("Base class:", Employee.__base__)
    print("Class namespace:", Employee.__dict__)
    print("Class name:", Employee.__name__)
    print("Module name:", Employee.__module__)
    print("Docstring:", Employee.__doc__)