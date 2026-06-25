'''
No exemplo anterior das linguagens de programação favoritas, se
armazenássemos as respostas de cada pessoa em uma lista, elas poderiam
escolher mais de uma linguagem predileta.
'''

# Passo 1: Definimos um dicionário chamado 'linguagens_favoritas'.
# Aqui, a chave é o nome da pessoa (uma string) e o valor associado é uma LISTA de linguagens.
# Usar uma lista como valor permite associar múltiplos elementos a uma única chave.
linguagens_favoritas = {
    'oliver': ['python', 'java'],
    'luis': ['java', 'c++', 'python'],
    'marceli': ['ruby', 'pearl', 'go']
}

# Passo 2: Usamos um loop 'for' para percorrer o dicionário.
# O método '.items()' nos devolve, a cada iteração, tanto a chave (nome) quanto o valor (a lista de linguagens).
for nome, linguagens in linguagens_favoritas.items():
    # Passo 3: Mostramos uma mensagem com o nome da pessoa.
    # O método '.title()' é usado para capitalizar a primeira letra do nome.
    print(f"{nome.title()} suas linguagens favoritas são:")
    
    # Passo 4: Como a variável 'linguagens' contém uma lista, precisamos de outro loop 'for'
    # (aninhado dentro do primeiro) para percorrer cada item individual dessa lista de linguagens.
    for linguagem in linguagens:
        # Passo 5: Imprimimos cada linguagem.
        # O caractere especial '\t' adiciona uma tabulação (recuo) para organizar visualmente o resultado.
        print(f"\t{linguagem.title()}")

