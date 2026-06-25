"""
CRIANDO LISTAS NUMÉRICAS

Há muitos motivos para armazenar um conjunto de números. Por
exemplo, você precisará manter um controle das posições de cada
personagem em um jogo, e talvez queira manter um registro das
pontuações mais altas de um jogador também.
"""
# Função range()
for value in range(1, 5):
    print(value)

'''
A função range() faz Python
começar a contar no primeiro valor que você lhe fornecer e parar quando
atingir o segundo valor especificado. Como ele para nesse segundo valor, a
saída não conterá o valor final, que seria 5, nesse caso
'''

for n in range(1, 6):
    print(n)
