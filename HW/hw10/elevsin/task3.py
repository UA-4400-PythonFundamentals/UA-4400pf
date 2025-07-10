class Employee:
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_employee(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def display_count(cls):
        print(f"Total employees: {cls.emp_count}")

    @classmethod
    def show_class_info(cls):
        print("(__base__):", cls.__base__)
        print("(__dict__):", cls.__dict__)
        print("(__name__):", cls.__name__)
        print("(__module__):", cls.__module__)
        print("(__doc__):", cls.__doc__)


e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)

Employee.display_count()

e1.display_employee()

print(Employee.show_class_info())