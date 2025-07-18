class InputError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data

def ask_age(age):
    try:
        age = int(age)
        if age < 0:
            raise InputError("InputError: age cannot be negative")
        else:
            if age % 2 == 0:
                return "Your age is even."
            return "Your age is odd."
    except ValueError:
        raise InputError("InputError: age must be an integer")
age = input("How old are you? ")
try: print(ask_age(age))
except InputError as e:
    print(e)