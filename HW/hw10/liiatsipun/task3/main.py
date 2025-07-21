class Employee():
    """An employee class, holding name, surname, and salary of every individual"""
    instances = 0

    def __init__(self, name, surname, salary):
        Employee.instances += 1
        self.name = name
        self.surname = surname
        self.salary = salary

    @staticmethod
    def employees_total():
        print(f"There're {Employee.instances} employees in total")

    def description(self):
        print(f'An employee {self.name} {self.surname} has a salary of {self.salary}')


liia = Employee('Liia', 'Tsipun', '10 000 UAH')
chunya = Employee('Chunya', 'Tsipun', '45g kamushkov')
chubik = Employee('Chubik', 'Morgunov', '60g kamushkov')

Employee.employees_total()
employees = [liia, chunya, chubik]
for emp in employees:
    emp.description()

print(f'Base class: {Employee.__base__}')
print(f'Namespae: {Employee.__dict__}')
print(f'Class name: {Employee.__name__}')
print(f'Definition module: {Employee.__module__}')
print(f'Docstring: {Employee.__doc__}')
