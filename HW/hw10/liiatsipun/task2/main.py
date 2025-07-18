class Human():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def welcome(self):
        print(f'Greetings {self.name} {self.surname}!')

    def species(self):
        print(f'{self.name} {self.surname} is a homosapien')

    @staticmethod
    def arbitrary_message():
        print('This is an arbitrary message from the static method')


liia = Human('Liia', 'Tsipun')
liia.welcome()
liia.species()
liia.arbitrary_message()
