class Employee:

    __doc__ = "Employee Class"
    counter = 0
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        Employee.counter += 1

    @classmethod
    def get_counter(cls):
        return cls.counter

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

    @classmethod
    def class_method(cls):
        print("(__base__):", cls.__base__)
        print("(__dict__):", cls.__dict__)
        print("(__name__):", cls.__name__)
        print("(__module__):", cls.__module__)
        print("(__doc__):", cls.__doc__)

rej = Employee("rej", 35, 20000)
rej.display()
mike = Employee("mike", 35, 20000)
mike.display()
print(Employee.get_counter())
Employee.class_method()