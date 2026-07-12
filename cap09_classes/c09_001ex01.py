"""
9.1 – Restaurante: 

1. Crie uma classe chamada Restaurant. O método __init__() de Restaurant deve
armazenar dois atributos: restaurant_name e cuisine_type.

2. Crie um método chamado describe_restaurant() que mostre essas duas
informações, e um método de nome open_restaurant() que exiba uma mensagem
informando que o restaurante está aberto.

3. Crie uma instância chamada restaurant a partir de sua classe. Mostre os dois
atributos individualmente e, em seguida, chame os dois métodos.
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
restaurante = Restaurante('Fogo de Chão', 'Brasileiro')

# Exibindo os atributos individualmente
print(f"Nome do restaurante: {restaurante.nome}")
print(f"Tipo de cuisine: {restaurante.tipoCuisine}")

# Chamando os métodos
restaurante.describe_restaurant()
restaurante.open_restaurant()
