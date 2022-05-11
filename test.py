from abc import ABC, abstractmethod

class A(ABC):
    
    @abstractmethod
    def price(self):
        '''price'''

class C(ABC):

    pass


class B(A, C):
    
    def price(self):
        return 100

    def __superclass__(self):
        return self.__class__.__bases__

ins = B()

print(ins.__superclass__())

