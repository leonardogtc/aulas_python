"""
9.4 – Pessoas atendidas: Comece com seu programa do Exercício 9.1 (página
225). Acrescente um atributo chamado number_served cujo valor default é 0. Crie
uma instância chamada restaurant a partir dessa classe. Apresente o número de
clientes atendidos pelo restaurante e, em seguida, mude esse valor e exiba-o
novamente.
Adicione um método chamado set_number_served() que permita definir o
número de clientes atendidos. Chame esse método com um novo número e mostre o
valor novamente.
Acrescente um método chamado increment_number_served() que permita
incrementar o número de clientes servidos. Chame esse método com qualquer
número que você quiser e que represente quantos clientes foram atendidos, por
exemplo, em um dia de funcionamento.
"""


class Restaurante():
    """Uma classe simples para modelar um restaurante."""

    def __init__(self, nome, tipoCuisine):
        """Inicializa os atributos do restaurante."""
        self.nome = nome.title()
        self.tipoCuisine = tipoCuisine.title()
        self.number_served = 0

    def describe_restaurant(self):
        """Exibe o nome e o tipo de cuisine do restaurante."""
        print(f"Nome do restaurante: {self.nome}")
        print(f"Tipo de cuisine: {self.tipoCuisine}")

    def open_restaurant(self):
        """Exibe uma mensagem informando que o restaurante está aberto."""
        print(f"O restaurante {self.nome} está aberto!")

    def set_number_served(self, number_served):
        """Define o número de clientes atendidos."""
        self.number_served = number_served

    def increment_number_served(self, number_served):
        """Incrementa o número de clientes servidos."""
        self.number_served += number_served

# Instanciando a classe Restaurante
restaurante = Restaurante('Fogo de Chão', 'Brasileiro')

# Apresentando o número de clientes atendidos
print(f"Clientes atendidos: {restaurante.number_served}")

# Mudando o valor do número de clientes atendidos
restaurante.set_number_served(10)
print(f"Clientes atendidos: {restaurante.number_served}")

# Incrementando o número de clientes servidos
restaurante.increment_number_served(5)
print(f"Clientes atendidos: {restaurante.number_served}")