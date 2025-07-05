class Employee:
    counter = 0
    def __init__(self, name, salary):
        Employee.counter += 1
        self.name = name    
        self.salary = salary

    def list_employees(self):
        return f'Total employees: {Employee.counter}'
    

    def employee_info(self):
        return f'Employee: {self.name}, Salary: {self.salary}'

Employee1 = Employee("Alice", 50000)
Employee2 = Employee("Bob", 60000)

print(Employee1.employee_info())
print(Employee2.employee_info())
print(Employee1.list_employees())

print(Employee.__name__)
print(Employee.__doc__)
print(Employee.__module__)
print(Employee.__dict__)
print(Employee.__base__)