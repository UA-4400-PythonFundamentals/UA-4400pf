class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

    @classmethod
    def get_species(cls):
        return f"Species: {cls.species}"

    @staticmethod
    def general_message():
        return "Nice to cya!"

person1 = Human("John")
person2 = Human("Jack")

person1.greet()
person2.greet()

print(Human.get_species())
print(Human.general_message())