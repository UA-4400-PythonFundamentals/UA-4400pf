class Employee:

    count = 0  

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def total_employees(cls):
        print(f"Total employees: {cls.count}")


e1 = Employee("Stive", 2000)
e2 = Employee("Jane", 3000)

e1.display_info()      
e2.display_info()       
Employee.total_employees()  


print("Base classes:", Employee.__base__)        
print("Namespace:", Employee.__dict__)           
print("Class name:", Employee.__name__)         
print("Module name:", Employee.__module__)       
print("Documentation:", Employee.__doc__)       