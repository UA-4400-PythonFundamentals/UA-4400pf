class X:
    def print(self):
        print("X.print")
class Y:
    def print(self):
        print("Y.print")
class Z():
    def print(self):
        print("Z.print")

class A(Y, X):
    pass
class B(Y, Z):
    pass
class M(A, B):
    pass


m = M()
m.print()
print(M.__mro__)