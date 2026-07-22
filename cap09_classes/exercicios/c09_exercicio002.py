"""
9.2 – Três restaurantes: Comece com a classe do Exercício 9.1. Crie três
instâncias diferentes da classe e chame describe_restaurant() para cada
instância.
"""

class Restaurante():
    """Uma classe simples para modelar um restaurante."""

    def __init__(self, nome, tipoCuisine):
        """Inicializa os atributos do restaurante."""
        self.nome = nome.title()
        self.tipoCuisine = tipoCuisine.title()

    def describe_restaurant(self):
        """Exibe o nome e o tipo de cuisine do restaurante."""
        print(f"Nome do restaurante: {self.nome}")
        print(f"Tipo de cuisine: {self.tipoCuisine}")

    def open_restaurant(self):
        """Exibe uma mensagem informando que o restaurante está aberto."""
        print(f"O restaurante {self.nome} está aberto!")

# Instanciando a classe Restaurante
restaurante1 = Restaurante('Fogo de Chão', 'Brasileiro')
restaurante2 = Restaurante('Madero', 'Americano')
restaurante3 = Restaurante('Japanese House', 'Asiático')

#Chamando o método describe_restaurant() para cada instância
restaurante1.describe_restaurant()
restaurante2.describe_restaurant()
restaurante3.describe_restaurant()