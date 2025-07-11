class Human:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

    @classmethod
    def species_info(cls):
        return "We are Homosapiens."

    @staticmethod
    def message():
        return "xo!"