class Human():
    def __init__(self, name):
        self.name=name


class Man(Human):
    def __init__(self, name='Adam'):
        super().__init__(name)


class Woman(Human):
    def __init__(self, name='Eve'):
        super().__init__(name)


class God():
    def __init__(self):
        self.creatures = [Man(), Woman()]

    def __getitem__(self, i):
        return self.creatures[i]
