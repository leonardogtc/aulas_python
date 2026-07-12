"""
Criando e usando uma classe
---------------------------
Uma classe é composta por 'atributos' e 'métodos' em que se define:
- atributo: são as características ou dados que descrevem os objetos criados a partir da classe (ex: nome, cor, tamanho).
- método: são as funções/ações que os objetos da classe podem executar (ex: falar, andar, calcular).
"""

# Por convenção, nomes com a primeira letra maiúscula referem-se a classes em Python


class Cachorro():
    """ Uma tentativa simples de modelar um cachorro. """

    # O método __init__() é chamado automaticamente sempre que criamos uma nova instância (objeto).
    # O primeiro parâmetro deste método é self, que é uma referência à própria instância.
    # Os parâmetros seguintes são os atributos que serão definidos na instância.
    # Em: def __init__(self, nome, idade):
    # self, nome e idade são os parâmetros que serão definidos na instância
    def __init__(self, nome, idade):
        """ Inicializa os atributos nome e idade. """
        self.nome = nome.title()        # Atributo nome
        self.idade = idade              # Atributo idade
        self.cor = ""                   # Atributo cor

    # O método sentar() é um método da classe Cachorro. Ele não é chamado automaticamente.
    # Ele é chamado quando criamos uma instância da classe Cachorro e chamamos o método sentar() nela.
    # Note que o primeiro parâmetro deste método é self, que é uma referência à própria instância.
    # Isso significa que o método sentar() tem acesso aos atributos da instância.
    # Em: def sentar(self):
    # self é o parâmetro que será definido na instância
    def sentar(self):
        """ Simula um cachorro sentando em resposta a um comando. """
        print(f"{self.nome} está sentado agora!")

    # O método rolar() é um método da classe Cachorro. Ele não é chamado automaticamente.
    # Ele é chamado quando criamos uma instância da classe Cachorro e chamamos o método rolar() nela.
    # Note que o primeiro parâmetro deste método é self, que é uma referência à própria instância.
    # Isso significa que o método rolar() tem acesso aos atributos da instância.
    # Em: def rolar(self):
    # self é o parâmetro que será definido na instância
    def rolar(self):
        """ Simula um cachorro rolando em resposta a um comando. """
        print(f"{self.nome} está rolando!")


# -----------------------------------------------------------------------------
# Criando um objeto a partir da classe Cachorro
# -----------------------------------------------------------------------------
meu_cachorro = Cachorro('banana', 10)
meu_cachorro.cor = 'caramelo'

# Acessando os atributos da classe
print(f"O nome do meu cachorro é {meu_cachorro.nome}.")
print(f"A idade do meu cachorro é {meu_cachorro.idade} anos.")
print(f"A cor do meu cachorro é {meu_cachorro.cor}.")

# chamando os métodos da classe Cachorro
meu_cachorro.sentar()
meu_cachorro.rolar()

# -----------------------------------------------------------------------------
# Criando várias instâncias
# -----------------------------------------------------------------------------
# Você pode criar tantas instâncias de uma classe quantas forem necessárias.
novo_cachorro = Cachorro('thor', 15)
novo_cachorro.cor = 'preto'

print(f"O nome do meu cachorro é {novo_cachorro.nome}.")
print(f"A idade do meu cachorro é {novo_cachorro.idade} anos.")
print(f"A cor do meu cachorro é {novo_cachorro.cor}.")

novo_cachorro.sentar()
novo_cachorro.rolar()
