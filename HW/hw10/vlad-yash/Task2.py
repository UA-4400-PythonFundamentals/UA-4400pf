#Task2. Create a class Human, everyone has a name,
# create a method in the class that displays a welcome message to each person.
# Create a class method in the class that returns information that it is a species
# of "Homosapiens". And in the class create a static method that returns an arbitrary message.

class Human:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!!!")
        
    @classmethod
    def species(cls):
        return "Species: \"Homosapiens\""
    
    def message():
        return "This is a static method!!!! Don't use it. It's empty, just a message..."
    
# a = Human("Vlad")
# a.greet()
# print(Human.species())
# print(Human.message())