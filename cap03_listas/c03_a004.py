# ==========================================
# Adicionando Elementos a uma Lista (.append)
# Este código demonstra o uso do método append(),
# que é a forma mais simples e direta de acrescentar
# um novo elemento ao final de uma lista.
# ==========================================

# Criando a lista inicial
motocicletas = ['honda', 'yamaha', 'suzuki']
print(motocicletas)

# 1. Adicionando um novo elemento ao final da lista
# O método append() pega o valor especificado e o insere na última posição da lista.
# A lista crescerá dinamicamente de tamanho 3 para tamanho 4.
motocicletas.append('kawazaki')
print(motocicletas)

# 2. Adicionando outro elemento ao final
# O valor 'ducati' será inserido logo após 'kawazaki'.
# O tamanho da lista agora passa a ser 5.
motocicletas.append('ducati')
print(motocicletas)

