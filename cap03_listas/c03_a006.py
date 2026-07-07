# ==========================================
# Inserindo Elementos em Posições Específicas
# Este código demonstra o uso do método insert().
# Ao contrário de append(), que adiciona itens ao final,
# insert() permite colocar um item em qualquer posição da lista.
# ==========================================

# Criando a lista inicial
motocicletas = ['honda', 'yamaha', 'suzuki']
print(motocicletas)

# 1. Inserindo um elemento na posição específica [1]
# O método insert(índice, valor) coloca 'ducati' no índice 1.
# IMPORTANTE: A 'yamaha' (que estava no índice 1) e todos os elementos a seguir
# são empurrados uma posição para a direita.
motocicletas.insert(1, 'ducati')
print(motocicletas)  # Resultado: ['honda', 'ducati', 'yamaha', 'suzuki']

# 2. Inserindo na posição do último elemento [-1]
# O índice [-1] representa o último elemento da lista no momento ('suzuki').
# Ao inserir em [-1], 'kawazaki' é colocada exatamente na posição onde estava
# a 'suzuki', empurrando-a para o final.
motocicletas.insert(-1, 'kawazaki')
print(motocicletas)  # Resultado: ['honda', 'ducati', 'yamaha', 'kawazaki', 'suzuki']

