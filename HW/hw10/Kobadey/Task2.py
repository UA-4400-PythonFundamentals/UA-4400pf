class human:

    species = "Homo sapiens"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello {self.name}, you are {self.age} years old."

    @classmethod
    def classmethod(cls):
        return f"You are {cls.species}."

    @staticmethod
    def staticmethod():
        return "Arbitrary message"

me = human("John", 22)
print(me.greet())
print(me.staticmethod())
print(human.classmethod())