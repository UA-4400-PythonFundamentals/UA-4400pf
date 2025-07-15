class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome, {self.name}!")

    def get_species(self):
        return "Homosapiens"

    @staticmethod
    def get_message():
        return "Humans are amazing creatures!"


person1 = Human("John")
person2 = Human("Alice")

person1.welcome()
person2.welcome()
print(person1.get_species())
print(Human.get_message())