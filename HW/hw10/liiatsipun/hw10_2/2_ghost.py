from random import randint


class Ghost():
    COLORS = ['white', 'yellow', 'purple', 'red']

    def __init__(self):
        self.color = Ghost.COLORS[randint(0, 3)]
