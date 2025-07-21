class Employee:
    """Class for company employees"""
    count = 0  # Лічильник співробітників

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    @classmethod
    def print_count(cls):
        print(f"Total employees: {cls.count}")

    def show_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

# Створення співробітників
emp1 = Employee("Ivan", 1000)
emp2 = Employee("Olena", 1500)

# Вивід інформації про співробітників
emp1.show_info()
emp2.show_info()

# Вивід кількості співробітників
Employee.print_count()

# Інформація про клас
print("Base classes:", Employee.__bases__)
print("Namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Docstring:", Employee.__doc__)