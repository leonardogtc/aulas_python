'''
Você foi contratado para fazer uma pesquisa de ranquear a linguagem de
programação mais utilizada por uma amostra populacional.
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

# Você ordena por contagem (decrescente) e depois por nome (crescente para desempate)
ranking = sorted(contagem_linguagens.items(), key=lambda x: (-x[1], x[0]))

# Exibe o ranking
print("linguagens ................... Posição")
print("-" * 40)

for posicao, (linguagem, quantidade) in enumerate(ranking, 1):
    # Formatar a saída com espaços para alinhamento
    espacos = 30 - len(linguagem)
    if espacos < 1:
        espacos = 1
    print(f"{linguagem}{' ' * espacos} {posicao}º lugar com {quantidade} voto(s)")
