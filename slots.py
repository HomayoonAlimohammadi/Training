class A:
    v = 10

    def __init__(self):
        self.x = 20


class B:
    __slots__ = "x", "y"

    def __init__(self):
        self.x = 20
        # self.y = 30


a = A()
print(A.__dict__)
print(a.__dict__)
b = B()
print(B.__dict__)
print(b.__slots__)
print(B.y)
print(b.x)
print(b.y)
