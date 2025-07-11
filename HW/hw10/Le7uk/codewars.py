# class Ball(object):
#     def __init__(self, ball_type="regular"):
#         self.ball_type = ball_type

# ===============================================

# class Ghost(object):
#     from random import choice

#     colors = ["white", "yellow", "purple", "red"]

#     def __init__(self):
#         self.color = Ghost.choice(Ghost.colors)

#     def __str__(self):
#         return f"Ghost color is {self.color}"

# ghost = Ghost()
# print(ghost.color) 

# ===============================

# class Human():
#         def __init__(self):
#             pass
# class Man(Human):
#         def __init__(self):
#             pass
# class Woman(Human):
#         def __init__(self):
#             pass   
# Taras = Man()
# Vika = Woman() 
# def God():
#     return [Taras, Vika]

# ==================================

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.info = f'{name}s age is {age}'

#     def __str__(self):
#         return f'Person: {self.name}, Age: {self.age}'

# ==================================
# import math
# class Sphere(object):
#     def __init__(self, radius,mass):
#         self.radius = radius
#         self.mass = mass

#     def get_volume(self):
#         return round((4/3) * math.pi * (self.radius ** 3),5)

#     def get_surface_area(self):
#         return round(4 * math.pi * (self.radius ** 2),5)
    
#     def get_radius(self):
#         return self.radius
    
#     def get_mass(self):
#         return self.mass
    
#     def get_density(self):
#         return round(self.mass / self.get_volume(),5)
    
#     =======================================

# def class_name_changer(cls,new_name):
#     if not new_name:
#         raise Exception("Name cannot be empty")
#     if not new_name[0].isupper():
#         raise Exception("Name must start with an uppercase letter")
#     if not new_name.isalnum():
#         raise Exception("Name must contain only alphanumeric characters")
    
#     cls.__name__ = new_name
#     return cls
   
