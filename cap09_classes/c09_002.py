"""
Trabalhando com instâncias da classe
------------------------------------
"""
class Car:
    """ Uma tentativa simples de representar um carro! """

    def __init__(self, make, model, year):
        """ Inicializa os atributos que descrevem o carro """
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """ Devolve um nome descritivo de maneira elegante """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())