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
    def __init__(self, state='Man'):
        super().__init__(state)


class Woman(Human):
    def __init__(self, state='Woman'):
        super().__init__(state)


def God():
    Adam = Man()
    Eve = Woman()
    first_peopls = [Adam, Eve]
    return first_peopls





# IV. Classy-classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f'{name}s age is {age}'




# V. Building Spheres
from math import sqrt, pow, pi


class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        p = self.get_density()
        return p * (4 / 3) * pi * pow(self.radius, 3)

    def get_volume(self):
        return (4 / 3) * pi * pow(self.radius, 3)

    def get_surface_area(self):
        return 4 * pi * pow(self.radius, 2)

    def get_density(self):
        return self.mass / self.get_volume()



# VI. Dynamic Classes

def class_name_changer(cls, new_name) :
    if not new_name[0].isupper() or not new_name.isalnum():
        raise NameError('Invalid class name!')
    cls.__name__ = new_name