class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def species_info(cls):
        return f"This is a species of {cls.species}."

    @staticmethod
    def arbitrary_message():
        return "Have a great day!"

if __name__ == "__main__":
    person = Human("Alice")
    person.welcome()
    print(Human.species_info())
    print(Human.arbitrary_message())