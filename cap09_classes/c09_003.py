"""
Herança
Nem sempre você precisará começar do zero para escrever uma classe. Se a
classe que você estiver escrevendo for uma versão especializada de outra
classe já criada, a herança poderá ser usada. Quando uma classe herda de
outra, ela assumirá automaticamente todos os atributos e métodos da
primeira classe. A classe original se chama classe-pai e a nova classe é a
classe-filha. A classe-filha herda todos os atributos e método de sua classe-
pai, mas também é livre para definir novos atributos e métodos próprios.

"""


class Carro():
    """Uma classe simples para representar um carro."""

    def __init__(self, marca, modelo, ano):
        """Inicializa os atributos do carro."""
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = 0

    def get_descriptive_name(self):
        """Devolve um nome descritivo de maneira elegante."""
        long_name = f"{self.ano} {self.marca} {self.modelo}"
        return long_name.title()


class CarroEletrico(Carro):
    """Um modelo de carro elétrico que representa um carro em especial."""

    def __init__(self, marca, modelo, ano):
        """Inicializa os atributos da classe-pai."""
        super().__init__(marca, modelo, ano)


meu_tesla = CarroEletrico('tesla', 'model 3', 2020)
print(meu_tesla.get_descriptive_name())

# pyrefly: ignore [parse-error]
"""
NOTA: A função super()
    A função super() em x é uma função especial que ajuda Python a criar
conexões entre a classe-pai e a classe-filha. Essa linha diz a Python para
chamar o método __init__() da classe-pai de ElectricCar.

    A vantagem de usar herança é que você não precisa repetir código. Você pode
manter os atributos e métodos da classe-pai e adicionar apenas os novos
recursos que você deseja para a classe-filha.

    Em resumo, se uma classe-filha recebe todos os atributos e métodos da
classe-pai, mas também tem novos atributos e métodos próprios, ela ainda é
uma versão especializada da classe-pai e a herança é a ferramenta certa para
implementá-la.
"""
