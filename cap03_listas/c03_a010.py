# ==========================================
# Ordenação de Listas: Permanente vs. Temporária
# Este código ensina como ordenar elementos de uma lista,
# diferenciando a ordenação definitiva (.sort()) da
# ordenação temporária (função sorted()).
# ==========================================

# Criando a lista inicial desordenada
carros = ['bmw', 'audi', 'toyota', 'subaru']
print(carros)

# 1. Ordenação permanente em ordem alfabética crescente com .sort()
# O método .sort() modifica a lista original de forma definitiva.
# Não há como voltar à ordem original após esta linha (a menos que a recriemos).
carros.sort()
print(carros)  # Exibirá: ['audi', 'bmw', 'subaru', 'toyota']

# 2. Ordenação permanente em ordem alfabética decrescente (inversa)
# Para isso, passamos o argumento nomeado reverse=True para o método .sort().
carros.sort(reverse=True)
print(carros)  # Exibirá: ['toyota', 'subaru', 'bmw', 'audi']

# 3. Ordenação temporária com a função sorted()
# Primeiro, recriamos a lista original na ordem antiga.
carros = ['bmw', 'audi', 'toyota', 'subaru']

# A função sorted(carros) nos devolve uma CÓPIA ordenada da lista,
# mas NÃO altera a lista original carros.
print(sorted(carros))  # Exibe a cópia ordenada: ['audi', 'bmw', 'subaru', 'toyota']
print(carros)          # A lista original continua intacta: ['bmw', 'audi', 'toyota', 'subaru']
