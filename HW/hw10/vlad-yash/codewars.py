# 10.2 Practical Tasks / [GitHub] [Outside]

# I. Ball-super-ball

class Ball(object):
    # your code goes here
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type
    

# II. Color-ghost

import random

class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])


# III. Basic-subclasses-Adam-and-Eve

def God():
    return ([adam, eve])
    
class Human:
    pass
class Man(Human):
    pass
class Woman(Human):
    pass
adam = Man()
eve = Woman()


# IV. Classy-classes

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.info=f"{self.name}s age is {self.age}"
        
    @property
    def getinfo(self):
        return self.info


# V. Building Spheres

import math

class Sphere(object):
    def __init__(self, radius: float, mass : float):
        self.radius = radius
        self.mass = mass
        
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return round((4/3) * math.pi * (self.radius**3), 5)
    
    def get_surface_area(self):
        return round(4 * math.pi * (self.radius**2), 5)
    
    def get_density(self):
        return round(self.mass / self.get_volume(), 5)
    

# VI. Dynamic Classes

def class_name_changer(cls, new_name):
    if not new_name[0].isupper() or not new_name.isalnum():
        raise ValueError("Incorrect new name")
    cls.__name__ = new_name