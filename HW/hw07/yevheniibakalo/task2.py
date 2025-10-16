def area(name, *values):
    if name == "circle" and len(values) == 1:
        return math.pi * values[0] ** 2
    elif name == "triangle" and len(values) == 2:
        return 0.5 * values[0] * values[1]
    elif name == "rectangle" and len(values) == 2:
        return values[0] * values[1]
    else:
        return "Unknown shape or wrong number of parameters"