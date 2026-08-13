"""
9.6 – Sorveteria: Uma sorveteria é um tipo específico de restaurante. 

- Escreva uma classe chamada IceCreamStand que herde da classe Restaurant escrita no
Exercício 9.1 (página 225) - arquivo: c09_exercicio001_restaurante.py ou no
Exercício 9.4 (página 232) - arquivo: c09_exercicio004_restaurante.py. Qualquer versão
da classe funcionará; basta escolher aquela de que você mais gosta.

- Adicione um atributo chamado flavors que armazene uma lista de sabores
de sorvete.

- Escreva um método para mostrar esses sabores.

- Crie uma instância de IceCreamStand e chame esse método.
"""

from c09_exercicio001_restaurante import Restaurante


class IceCreamStand(Restaurante):
    def __init__(self, nome, tipoCuisine):
        """Inicializa os atributos da sorveteria."""
        super().__init__(nome, tipoCuisine)
        self.flavors = ['baunilha', 'chocolate', 'morango']

    def show_flavors(self):
        """Exibe os sabores de sorvete."""
        print("Sabores disponíveis:")
        for flavor in self.flavors:
            print(f"- {flavor}")


IceCreamStand("Sorveteria do Zé", "Doceria").show_flavors()