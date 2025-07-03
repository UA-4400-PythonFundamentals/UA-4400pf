def largerNumber(a, b):
    """
    Returns the larger of two numbers.
    """
    return a if a > b else b

x = int(input("Перше число: "))
y = int(input("Друге число: "))

larger = largerNumber(x, y)
print(f"Більше число: {larger}")