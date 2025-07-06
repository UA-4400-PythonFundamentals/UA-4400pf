class Employee:
    """Create an employ"""
    count_employs = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

        Employee.count_employs += 1

    @classmethod
    def print_total_num_of_employs(cls):
        return f'Total number of employs : {cls.count_employs}'


    def display_information(self):
        return f"Employ name: {self.name}, salary: {self.salary}"



if __name__ == "__main__":
    employs = [Employee('John', 100),Employee('Tom', 200), Employee('Ann', 300) ]

    print(Employee.__base__)
    print(Employee.__dict__)
    print(Employee.__name__)
    print(Employee.__module__)
    print(Employee.__doc__)


    for employ in employs:
        print(employ.display_information())

    print(Employee.print_total_num_of_employs())