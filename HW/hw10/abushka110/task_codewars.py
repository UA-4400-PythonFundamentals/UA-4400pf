# I. Ball-super-ball
class Ball(object):
    def __init__(self, ball_type="regular"):
            self.ball_type = ball_type


# II. Color-ghost
from random import choice

class Ghost(object):
    colors = ["white", "yellow", "purple", "red"]

    def __init__(self):
        self.color = choice(Ghost.colors)


# III. Basic-subclasses-Adam-and-Eve
class Human():
    def __init__(self, state):
        self.state = state

class Man(Human):
    def __init__(self, state="Man"):
        super().__init__(state)

class Woman(Human):
    def __init__(self, state="Woman"):
        super().__init__(state)
        
def God():
    Adam = Man()
    Eve = Woman()
    first_people = [Adam, Eve]
    return first_people


# IV. Classy-classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f'{name}s age is {age}'


# V. Building Spheres
import math

class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        volume = (4/3) * math.pi * self.radius**3
        return round(volume, 5)

    def get_surface_area(self):
        surface_area = 4 * math.pi * self.radius**2
        return round(surface_area, 5)

    def get_density(self):
        volume = (4/3) * math.pi * self.radius**3
        density = self.mass / volume
        return round(density, 5)


# VI. Dynamic Classes
def class_name_changer(cls, new_name):
    if not new_name or not new_name[0].isupper() or not new_name.isalnum():
        raise ValueError("Invalid class name. It must start with an uppercase letter and contain only alphanumeric characters.")
    
    cls.__name__ = new_name
    return cls

