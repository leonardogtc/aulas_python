# ==========================================
# Alteração de Valores de uma Lista
# Este código demonstra como listas são mutáveis,
# ou seja, como podemos alterar o valor de um
# elemento que já existe na lista usando seu índice.
# ==========================================

# Criando a lista inicial com três elementos (motocicletas)
motocicletas = ['honda', 'yamaha', 'suzuki']
print(motocicletas)

# 1. Substituindo o primeiro elemento da lista (Honda por Ducati)
# Acessamos a posição [0] e atribuímos um novo valor ('ducati') a ela.
# Isso sobrescreve o valor anterior permanentemente.
motocicletas[0] = 'ducati'
print(motocicletas)

# 2. Substituindo o terceiro elemento da lista (Suzuki por Kawasaki)
# O índice correspondente ao terceiro elemento é [2].
# Também há um pequeno erro de digitação no original ('kawazaki' com z, mantido para coerência).
motocicletas[2] = 'kawazaki'
print(motocicletas)

