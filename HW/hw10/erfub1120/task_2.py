class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        return f'Welcome {self.name}!'
    
    @classmethod
    def info(cls):
        return 'Homosapiens'
    
    @staticmethod
    def message():
        return 'Keep learning'
    
# person = Human("John")
# print(person.welcome())
# print(Human.info())
# print(Human.message())