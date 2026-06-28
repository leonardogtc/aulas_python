'''
Com frequência, você achará útil passar uma lista para uma função, seja
uma lista de nomes, de números ou de objetos mais complexos, como
dicionários.
'''

# Passando uma lista como argumento


def saudando_usuarios(nomes):
    """ Exibe uma saudação simples a cada usuário da lista """
    for nome in nomes:
        msg = f"Olá, {nome}!"
        print(msg)


usernames = ['leonardo', 'oliver', 'lucia', 'giovanna', 'ayme']


saudando_usuarios(usernames)
