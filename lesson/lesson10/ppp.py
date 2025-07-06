
class Coputter:
    def __init__(self):
        self.price = 100
        self._price = 80
        self.__price = 50
    def __str__(self):
        return f"Coputter(price={self.price}, _price={self._price}, __price={self.__price})"

c = Coputter()
print(c)           # Coputter(price=100, _price=80, __price=50)
print(c.price)      # 100
print(c._price)     # 80
# print(c.__price)     # AttributeError: 'Coputter' object has no attribute '__price'
print(c._Coputter__price)  # 50 (accessing the name-mangled attribute)