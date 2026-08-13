# CONCEITO: Argumentos Nomeados Arbitrários (**kwargs)
# ----------------------------------------------------
# Dois asteriscos (**) antes do nome de um parâmetro (ex: **user_info) dizem ao Python
# para empacotar todos os argumentos nomeados extras em um DICIONÁRIO (chave: valor).
# É útil quando não sabemos previamente quais atributos adicionais o usuário fornecerá.

# 'primeiro' e 'ultimo' são parâmetros posicionais obrigatórios.
# '**user_info' irá capturar quaisquer outros pares chave=valor fornecidos na chamada.
def criar_perfil(primeiro, ultimo, **user_info):
    """Constrói um dicionário contendo tudo o que sabemos sobre um usuário."""
    profile = {}
    # Atribui o primeiro nome e sobrenome às chaves do dicionário 'profile'
    profile['primeiro_nome'] = primeiro
    profile['sobrenome'] = ultimo

    # Percorre os pares chave (key) e valor (value) do dicionário **user_info gerado automaticamente
    for key, value in user_info.items():
        profile[key] = value

    # Retorna o dicionário completo consolidado
    return profile


# Chamada da função:
# 'albert' -> primeiro
# 'einstein' -> ultimo
# location='princeton', field='physics' -> vão para o dicionário **user_info
user_profile = criar_perfil(
    'albert', 'einstein', location='princeton', field='physics')

# Exibe o dicionário final gerado
print(user_profile)
