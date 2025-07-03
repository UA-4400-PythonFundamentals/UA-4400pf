class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f'Welcome {self.name}'


    @classmethod
    def information(cls):
        return 'Homosapiens'


    @staticmethod
    def message():
        return 'Kind people'