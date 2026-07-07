class Cachorro():
    """ Uma tentativa simples de modelar um cachorro! """

    def __init__(self, nome, idade):
        """ Inicializa os atributos nome e idade """
        self.nome = nome
        self.idade = idade

    def sentar(self):
        """ Simula um cachorro sentando em resposta a um comando. """
        print(f"{self.nome.title()} está sentado agora!")

    def rolar(self):
        """ Simula um cachorro rolando em resposta a um comando. """
        print(f"{self.nome.title()} está rolando!")