import random
from utils import generate_random_full_name


class Hummen:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

    def __repr__(self):
        return f"{self.name} {self.age})"

    def __lt__(self, other):
        """Compare Hummen objects based on age."""
        if not isinstance(other, Hummen):
            return NotImplemented
        return self.age < other.age

    def rename(self, new_name: str):
        """Rename the Hummen."""
        self.name = new_name


hummens = [
    Hummen("Alice", 30),
    Hummen("Bob", 25),
    Hummen("Charlie", 35),
    Hummen("David", 20),
    Hummen("Eve", 28),
]
hummens.sort()  # Sort by age using the __lt__ method
print(hummens)
for hum in hummens:
    if hum.age % 2:
        hum.rename(f"{hum.name} (young)")
    else:
        hum.rename(f"{hum.name} (old)")
print(hummens)


class User(Hummen):
    def __init__(self, name: str, age: int, email: str):
        super().__init__(name, age)
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.age}), Email: {self.email}"


workers = []
for i in range(10):
    age = random.randint(0, 65)
    name = generate_random_full_name()
    email = f"{name.lower().replace(' ', '.')}@example.com"
    if age < 18:
        workers.append(Hummen(name, age))
    else:
        workers.append(User(name, age, email))
workers.sort()  # Sort by age using the __lt__ method
from pprint import pprint

pprint(workers)
# print(workers)
for user in workers:
    print(user)

for hum in workers:
    if hum.age< 16:
        hum.rename(f"{hum.name} (young)")
    else:
        hum.rename(f"{hum.name} (old)")
print(workers)
