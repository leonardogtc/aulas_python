"""
9.3 – Usuários: Crie uma classe chamada User. Crie dois atributos de nomes
first_name e last_name e, então, crie vários outros atributos normalmente
armazenados em um perfil de usuário. Escreva um método de nome
describe_user() que apresente um resumo das informações do usuário. Escreva
outro método chamado greet_user() que mostre uma saudação personalizada ao
usuário.
Crie várias instâncias que representem diferentes usuários e chame os dois
métodos para cada usuário
"""

class Usuario():
    """Uma classe para modelar um usuário."""

    def __init__(self, nome, sobrenome):
        """Inicializa os atributos do usuário."""
        self.nome = nome.title()
        self.sobrenome = sobrenome.title()

    def describe_user(self):
        """Exibe um resumo das informações do usuário."""
        print(f"Nome do usuário: {self.nome}")
        print(f"Sobrenome do usuário: {self.sobrenome}")

    def greet_user(self):
        """Exibe uma saudação personalizada ao usuário."""
        print(f"Olá, {self.nome} {self.sobrenome}!")

# Instanciando a classe Usuario
usuario1 = Usuario('Leonardo', 'Rodrigues')
usuario2 = Usuario('Maria', 'Silva')

# Chamando o método describe_user() para cada instância
usuario1.describe_user()
usuario2.describe_user()

# Chamando o método greet_user() para cada instância
usuario1.greet_user()
usuario2.greet_user()