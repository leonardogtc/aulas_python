"""
9.5 – Tentativas de login: Acrescente um atributo chamado login_attempts à sua classe User do Exercício 9.3 (página 226). Escreva um método chamado increment_login_attempts() que incremente o valor de login_attempts em 1. 
Escreva outro método chamado reset_login_attempts() que reinicie o valor de login_attempts com 0.
Crie uma instância da classe User e chame increment_login_attempts() várias vezes. Exiba o valor de login_attempts para garantir que ele foi incrementado de forma apropriada e, em seguida, chame reset_login_attempts(). Exiba login_attempts novamente para garantir que seu valor foi reiniciado com 0.
"""


class Usuario():
    """Uma classe para modelar um usuário."""

    def __init__(self, nome, sobrenome):
        """Inicializa os atributos do usuário."""
        self.nome = nome.title()
        self.sobrenome = sobrenome.title()
        self.login_attempts = 0

    def increment_login_attempts(self):
        """Incrementa o valor de login_attempts em 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reinicia o valor de login_attempts com 0."""
        self.login_attempts = 0

    def describe_user(self):
        """Exibe um resumo das informações do usuário."""
        print(f"Nome do usuário: {self.nome}")
        print(f"Sobrenome do usuário: {self.sobrenome}")
        print(f"Tentativas de login: {self.login_attempts}")

usuario = Usuario('Leonardo', 'Rodrigues')
usuario.increment_login_attempts()
usuario.increment_login_attempts()
usuario.increment_login_attempts()
usuario.describe_user()
usuario.reset_login_attempts()
usuario.describe_user()

    