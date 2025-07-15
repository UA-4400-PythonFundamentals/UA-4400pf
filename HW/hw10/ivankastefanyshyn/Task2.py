class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def species_message(cls):
        print(f"Species: 'Homosapiens'.")

    @staticmethod
    def arbitrary_message():
        print(f"Be happy!!!")


a = Human(input("Please enter your name:"))
a.welcome_message()
Human.species_message()
Human.arbitrary_message()
