class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

    def __str__(self):
        return f"Hello {self.name} "
    
    
    def is_human(self):
        return  "You are Homosapiens"
    
    
    @staticmethod
    def smth():
        return "This is a static method"
    
Taras = Human("Taras", 20)
print(Taras)
print(Taras.is_human())