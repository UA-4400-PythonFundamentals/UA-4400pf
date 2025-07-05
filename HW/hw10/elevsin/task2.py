class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome {self.name}")

    @classmethod
    def get_species(cls):
        return f"Species: {cls.species}"

    @staticmethod
    def arbitrary_message():
        return "This is a static method!"


alice = Human("Alice")
alice.welcome()

print(Human.get_species())

print(Human.arbitrary_message())