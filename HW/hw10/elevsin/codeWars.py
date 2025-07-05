# I. Ball-super-ball
class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

# II. Color-ghost
import random
class Ghost(object):
    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]
        self.color = random.choice(colors)

# III. Basic-subclasses-Adam-and-Eve
def God():
    return [Man(), Woman()]

class Human(object):
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

# IV. Classy-classes
class Person:
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"

# V. Building Spheres
import math

class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        self._volume_exact = (4.0 / 3.0) * math.pi * self.radius ** 3

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round(self._volume_exact, 5)

    def get_surface_area(self):
        area = 4.0 * math.pi * self.radius ** 2
        return round(area, 5)

    def get_density(self):
        density = self.mass / self._volume_exact
        return round(density, 5)

# VI. Dynamic Classes
import re

def class_name_changer(cls, new_name):
    if not re.fullmatch(r'[A-Za-z0-9]+', new_name) or not new_name[0].isupper():
        raise ValueError("Invalid class name")
    cls.__name__ = new_name
    cls.__qualname__ = new_name
    return cls

