# Task1
myFunc = lambda a,b: a if a > b else b

# Task2
def area(name, *values):
    if name == "circle" and len(values) == 1:
        return 3.14 * values[0] ** 2
    elif name == "triangle" and len(values) == 2:
        return 0.5 * values[0] * values[1]
    elif name == "rectangle" and len(values) == 2:
        return values[0] * values[1]
    else:
        return "Unknown shape"

# Task3

def numberOfCharacters(str):
    test = {}
    for i in str:
        test.update({i: str.count(i)})
    return test
