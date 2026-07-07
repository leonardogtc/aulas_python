# ==========================================
# Removendo Itens com a Instrução del
# Este código demonstra como remover elementos
# de uma lista permanentemente a partir de seu índice
# usando a palavra-chave reservada 'del'.
# ==========================================

# NOTA DIDÁTICA:
# Você pode remover um item de qualquer posição usando:
# del nome_da_lista[indice]
# (Atenção: Não há ponto entre a palavra "del" e o nome da lista!)

# Lista inicial com 5 elementos
motocicletas = ['honda', 'yamaha', 'suzuki', 'ducati', 'kawazaki']
print(motocicletas)

# 1. Apagando elemento na 5ª posição (índice [4])
# O elemento no índice 4 é 'kawazaki'. Ao deletá-lo, a lista reduz de tamanho
# e o item é eliminado permanentemente da memória.
del motocicletas[4]
print(motocicletas)  # Resultado: ['honda', 'yamaha', 'suzuki', 'ducati']

# 2. Apagando o novo último elemento com del [-1]
# O índice [-1] agora representa 'ducati' (pois 'kawazaki' já foi removida).
# Ao executar a linha abaixo, 'ducati' será deletada da lista.
del motocicletas[-1]
print(motocicletas)  # Resultado: ['honda', 'yamaha', 'suzuki']

