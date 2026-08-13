# CONCEITO: Passando Listas como Argumento para Funções
# -----------------------------------------------------
# Quando passamos uma lista para uma função, a função obtém acesso direto aos elementos dessa lista.
# Isso permite percorrer (iterar sobre) a lista ou realizar operações em lote com seus dados.

# A função recebe o parâmetro 'nomes', que espera receber uma estrutura iterável (como uma lista)
def saudando_usuarios(nomes):
    """Exibe uma saudação simples a cada usuário da lista."""
    # O laço 'for' percorre elemento por elemento da lista recebida
    for nome in nomes:
        # Formata a mensagem com a primeira letra maiúscula usando .title() ou string direta
        msg = f"Olá, {nome.title()}!"
        # Exibe a mensagem de saudação individual
        print(msg)


# Criamos uma lista contendo 5 nomes de usuários
usernames = ['leonardo', 'oliver', 'lucia', 'giovanna', 'ayme']

# Chamamos a função 'saudando_usuarios' passando a lista 'usernames' inteira como argumento
saudando_usuarios(usernames)
