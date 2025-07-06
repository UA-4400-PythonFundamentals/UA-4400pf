# Task 1
class Ball:
    def __init__(self, type="regular"):
        self.type = type

# Task 2
from random import choice

class Ghost:
    colors = ["white", "yellow", "purple", "red"]

    def color(self):
        return choice(self.colors)
    
# Task 3
class Human:
    def __init__(self, state):
        self.state = state

class Man(Human):
    def __init__(self, state):
        super().__init__(state)
        
class Woman(Human):
    def __init__(self, state):
        super().__init__(state)

# Task 4
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f'{name}s age is {age}'
        
# Task 5
from math import pi
class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return (4/3) * pi * (self.radius ** 3)
    
    def get_surface_area(self):
        return 4 * pi * (self.radius ** 2)
    
    def get_density(self):
        return self.mass / self.get_volume()
    
# Task 6
def class_name_changer(cls, new_name):
    cls.__name__ = new_name
    return cls

