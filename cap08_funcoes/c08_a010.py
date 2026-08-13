# CONCEITO: Devolvendo Dicionários a Partir de Funções
# ----------------------------------------------------
# Funções podem construir e retornar estruturas de dados complexas, como dicionários e listas.
# Isso é fundamental para organizar dados estruturados (ex: registros de usuários, produtos, etc).

# A função recebe 'nome', 'sobrenome' e opcionalmente 'idade'
def criando_pessoa(nome, sobrenome, idade=''):
    """Devolve um dicionário com informações sobre uma pessoa."""
    # Se a idade for informada (diferente de string vazia ou None)
    if idade:
        # Monta o dicionário contendo as três chaves: nome, sobrenome e idade
        pessoa = {
            'nome': nome,
            'sobrenome': sobrenome,
            'idade': idade,
        }
    else:
        # Monta o dicionário contendo apenas nome e sobrenome
        pessoa = {
            'nome': nome,
            'sobrenome': sobrenome,
        }
    # Retorna a estrutura de dicionário criada
    return pessoa


# Chamada 1: Sem fornecer idade. O dicionário retornado terá 2 pares chave-valor.
pessoa = criando_pessoa('Oliver', 'Conceição')
print(pessoa)  # Imprime: {'nome': 'Oliver', 'sobrenome': 'Conceição'}

# Chamada 2: Fornecendo a idade (56). O dicionário retornado terá 3 pares chave-valor.
pessoa1 = criando_pessoa('Leonardo', 'Conceição', 56)
print(pessoa1)  # Imprime: {'nome': 'Leonardo', 'sobrenome': 'Conceição', 'idade': 56}
