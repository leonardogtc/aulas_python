# Usando argumentos nomeados arbitrários
# --------------------------------------
# Às vezes, você vai querer aceitar um número arbitrário de argumentos, mas
# não saberá com antecedência qual tipo de informação será passado para a
# função. Nesse caso, podemos escrever funções que aceitem tantos pares
# chave-valor quantos forem fornecidos pela instrução que faz a chamada.
# Um exemplo envolve criar perfis de usuários: você sabe que obterá
# informações sobre um usuário, mas não tem certeza quanto ao tipo de
# informação que receberá.

def criar_perfil(primeiro, ultimo, **user_info):
    """ Constrói um dicionário contendo tudo oque sabemos sobre um usuário. """
    profile = {}
    profile['primeiro_nome'] = primeiro
    profile['sobrenome'] = ultimo
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = criar_perfil(
    'albert', 'einstein', location='princeton', field='physics')

print(user_profile)
