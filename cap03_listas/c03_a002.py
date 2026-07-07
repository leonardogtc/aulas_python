# ==========================================
# Exibição e Acesso a Valores de uma Lista
# Este código demonstra como acessar elementos
# de uma lista usando índices positivos e negativos,
# e como formatar textos obtidos da lista.
# ==========================================

# Criando uma lista de modelos de bicicletas.
# Cada modelo é um elemento da lista, separado por vírgula.
bicicletas = ['caloi', 'monark', 'trak', 'redline', 'specialized', 'bmx']

# 1. Acessando e exibindo a lista completa
# Exibe a lista exatamente como foi definida, incluindo colchetes e aspas.
print(bicicletas)

# 2. Acessando a segunda posição [1]
# Lembre-se: em programação, a contagem quase sempre começa em ZERO.
# Índice [0] = 'caloi' (1º elemento)
# Índice [1] = 'monark' (2º elemento)
print(bicicletas[1])

# 3. Acessando a PRIMEIRA posição [0]
# O primeiro elemento de qualquer lista sempre estará no índice 0.
print(bicicletas[0])

# 4. Acessando a ÚLTIMA posição [-1]
# O Python permite o uso de índices negativos para contar de trás para frente.
# O índice [-1] sempre retorna o último elemento da lista, não importa o tamanho dela.
print(bicicletas[-1])

# 5. Acessando a PENÚLTIMA posição [-2]
# O índice [-2] retorna o segundo elemento de trás para frente (neste caso, 'specialized').
print(bicicletas[-2])

# 6. Modificando a string de saída com métodos de texto (String)
# Como bicicletas[1] é uma String ('monark'), podemos aplicar qualquer método de String a ela.
# .title() coloca a primeira letra em maiúscula (exibe: Monark).
print(bicicletas[1].title())

# .upper() coloca todas as letras em maiúscula (exibe: BMX).
print(bicicletas[-1].upper())

