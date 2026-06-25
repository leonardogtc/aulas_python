'''
FATIAS DE UMA LISTA
'''

jogadores = ['oliver', 'gustavo', 'guto', 'ezequiel', 'leonardo']

# Exbindo uma fatia dos 3 primeiros jogadores
print(jogadores[0:3])

# Exibindo uma fatia dos 2 últimos jogadores
# Se o índice final for omitido o python correrá da posição indicada até o final da lista
print(jogadores[3:])

# O mesmo acontece com o inínio - começará do início do range - posição 0
print(jogadores[:3])

# Exibindo fatia com jogadores do meio da lista
print(jogadores[1:4])

# Esse código exibe os nomes dos três últimos jogadores e continuaria a
# funcionar à medida que a lista de jogadores mudar de tamanho.
print(jogadores[-3:])

# Percorrendo a lista
for jogador in jogadores[:3]:
    print(jogador.title())
