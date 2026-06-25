'''
Você foi contratado para fazer uma pesquisa de ranquear a linguagem de
programação mais utilizada por uma amostra populacional.

NOTA: Versão alterada para permitir empate em mesma posição do ranking
'''

# Você coleta os dados. Resolveu fazer isso utilizando um dictionary.
linguagens_favoritas = {
    'oliver': 'python',
    'leonardo': 'java',
    'ayme': 'rust',
    'lucia': 'c++',
    'ivonete': 'c ansi',
    'tatiana': 'java',
    'giovanna': 'c++',
    'murilo': 'c++',
    'fernanda': 'python',
    'ezequiel': 'python',
    'martins': 'rust',
    'fabiane': 'python',
    'carnegie': 'java',
    'guto': 'python',
    'gustavo': 'c++',
    'joão': 'java',
    'adriana': 'java'
}

# Você precisa contar as ocorrências de cada linguagem
contagem_linguagens = {}
for linguagem in linguagens_favoritas.values():
    contagem_linguagens[linguagem] = contagem_linguagens.get(linguagem, 0) + 1

# Ordenar por contagem (decrescente)
linguagens_ordenadas = sorted(contagem_linguagens.items(), key=lambda x: -x[1])

# Exibe o ranking
print("linguagens ................... Posição")
print("-" * 40)

posicao = 1
for i, (linguagem, quantidade) in enumerate(linguagens_ordenadas):
    # Verificar se há empate com o anterior
    if i > 0 and quantidade == linguagens_ordenadas[i-1][1]:
        # Mantém a posição em caso de empate
        posicao_atual = posicao
    else:
        posicao_atual = i + 1
        posicao_atual = posicao_atual

    espacos = 30 - len(linguagem)
    if espacos < 1:
        espacos = 1
    print(f"{linguagem}{' ' * espacos} {posicao_atual}º lugar com {quantidade} voto(s)")
