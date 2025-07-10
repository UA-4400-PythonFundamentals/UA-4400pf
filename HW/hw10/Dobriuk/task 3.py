class Employee:
    employee_count = 0
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    @classmethod
    def show_total(cls) -> None:
        print(f"Total number of employees: {cls.employee_count}")
    
    def show_info(self) -> None:
        print(f"Name: {self.name}, Salary: {self.salary}")

    def __repr__(self) -> str:
        return f"Employee({self.name}, {self.salary})"

if __name__ == "__main__":

    staff = [Employee("Oleksandr", 50_000),
             Employee("David", 60_000)]

    for emp in staff:
        emp.show_info()
    Employee.show_total()

    print("Base class:", Employee.__base__)
    print("Namespace:", list(Employee.__dict__.keys()))
    print("Class name:", Employee.__name__)
    print("Module name:", Employee.__module__)
    print("Docstring:", Employee.__doc__)