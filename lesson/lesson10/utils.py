import random

first_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
last_names = ["Smith", "Jones", "Williams", "Brown", "Davis"]

def generate_random_full_name():
    first = random.choice(first_names)
    last = random.choice(last_names)
    return f"{first} {last}"
