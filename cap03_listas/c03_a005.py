# ==========================================
# Construindo Listas de Forma Dinâmica
# Este código demonstra um padrão muito comum na programação:
# começar com uma lista vazia e, conforme o programa
# executa, ir adicionando itens a ela dinamicamente.
# ==========================================

# 1. Criando uma lista totalmente vazia
motocicletas = []
print(motocicletas)  # Mostrará apenas os colchetes sem nada dentro: []

# 2. Adicionando itens consecutivamente
# Cada chamada de .append() adiciona o novo item na última posição da lista.
# O primeiro adicionado ('honda') fica no índice [0].
motocicletas.append('honda')

# 'yamaha' é inserido no final, ficando no índice [1].
motocicletas.append('yamaha')

# 'suzuki' é inserido no final, ficando no índice [2].
motocicletas.append('suzuki')

# 3. Exibindo o resultado final
# Exibirá a lista completa com os três elementos adicionados em ordem.
print(motocicletas)

