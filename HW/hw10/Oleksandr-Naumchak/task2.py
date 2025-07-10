#Task2. Create a class Human, everyone has a name,
# create a method in the class that displays a welcome message to each person.
# Create a class method in the class that returns information that it is a species
# of "Homosapiens". And in the class create a static method that returns an arbitrary message.

class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

    @classmethod
    def get_species(cls):
        return f"This species is {cls.species}"

    @staticmethod
    def message():
        return "This is a static method returning an arbitrary message."

# Пример:
h = Human("Aleks")
h.greet()
print(Human.get_species())
print(Human.message())