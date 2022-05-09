from abc import ABC, abstractmethod

class Product(ABC):

    @abstractmethod
    def cook(self):
        pass

class FettuccineAlfredo(Product):
    name = "Fettuccine Alfredo"
    def cook(self):
        print("Italian main course prepared: "+self.name)

class Tiramisu(Product):
    name = "Tiramisu"
    def cook(self):
        print("Italian dessert prepared: "+self.name)

class DuckALOrange(Product):
    name = "Duck À L'Orange"
    def cook(self):
        print("French main course prepared: "+self.name)

class CremeBrulee(Product):
    name = "Crème brûlée"
    def cook(self):
        print("French dessert prepared: "+self.name)

class Factory(ABC):

	@staticmethod
	@abstractmethod
	def get_dish(type_of_meal):
		pass

class ItalianDishesFactory(Factory):
    def get_dish(type_of_meal):
        if type_of_meal == "main":
            return FettuccineAlfredo()
        if type_of_meal == "dessert":
            return Tiramisu()

    def create_dessert(self):
        return Tiramisu()

class FrenchDishesFactory(Factory):
    def get_dish(type_of_meal):
        if type_of_meal == "main":
            return DuckALOrange()

        if type_of_meal == "dessert":
            return CremeBrulee()

class FactoryProducer:
    def get_factory(self, type_of_factory):
        if type_of_factory == "italian":
            return ItalianDishesFactory
        if type_of_factory == "french":
            return FrenchDishesFactory


fp = FactoryProducer()

fac = fp.get_factory("italian")
main = fac.get_dish("main")
main.cook()
dessert = fac.get_dish("dessert")
dessert.cook()

fac1 = fp.get_factory("french")
main = fac1.get_dish("main")
main.cook()
dessert = fac1.get_dish("dessert")
dessert.cook()