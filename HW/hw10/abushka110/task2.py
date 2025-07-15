class Human:
    def __init__(self, name: str):
        self.name = name
    
    def welcome_message(self):
        return f"Welcome to the Python World {self.name}"
    
    @classmethod
    def info(cls):
        return "Homosapiens"
    
    @staticmethod
    def message():
        return "You are not a robot"
    

if __name__ == "__main__":
    person1 = Human("John")
    print(person1.welcome_message())

    print(Human.info())
    print(Human.message()) 