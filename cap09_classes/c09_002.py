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
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ Devolve um nome descritivo de maneira elegante """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """ Exibe a quilometragem do carro """
        print(f"Este carro tem {self.odometer_reading} milhas.")

    def update_odometer(self, mileage):
        """ Atualiza a quilometragem """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Você não pode reverter a quilometragem!")

    def increment_odometer(self, mileage):
        """ Adiciona a milhagem ao valor atual """
        if mileage >= 0:
            self.odometer_reading += mileage
        else:
            print("Você não pode reverter a quilometragem!")


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

# Modificando o valor do atributo
my_new_car.odometer_reading = 23

# Moficiando por meio de um método
my_new_car.update_odometer(23500)

# Adicionando milhagem ao valor atual
my_new_car.increment_odometer(100)

# Mostrando o valor do atributo
my_new_car.read_odometer()

