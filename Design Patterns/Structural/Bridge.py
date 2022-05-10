from abc import ABC, abstractmethod


class Material(ABC):

    @abstractmethod
    def __str__(self):
        '''Display name of the material'''


class Stone(Material):

    def __str__(self):
        return self.__class__.__name__


class Wooden(Material):

    def __str__(self):
        return self.__class__.__name__


class Building(ABC):

    @abstractmethod
    def __str__(self):
        '''Display name of the structure'''

    
class Tower(Building):

    def __init__(self, name, material: Material):
        self.name = name
        self.material = material

    def __str__(self):
        return str(self.material) + ' ' + self.__class__.__name__ + ' ' + self.name


class Wall(Building):

    def __init__(self, name, material: Material):
        self.name = name
        self.material = material

    def __str__(self):
        return str(self.material) + ' ' + self.__class__.__name__ + ' ' + self.name


stone = Stone()
wall = Wall(name='Main Wall', material=stone)

wood = Wooden()
tower = Tower(name='Main Tower', material=wood)

print(wall)
print(tower)

