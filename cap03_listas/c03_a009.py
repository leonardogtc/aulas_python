# ==========================================
# Removendo Itens por Valor com .remove()
# Se você sabe qual é o valor que quer apagar,
# mas não sabe em qual índice (posição) ele está,
# o método remove() é a escolha ideal.
# ==========================================

# Lista inicial com 5 elementos
motocicletas = ['honda', 'yamaha', 'suzuki', 'ducati', 'kawazaki']
print(motocicletas)

# Definimos uma variável com o valor que queremos procurar e remover
muito_cara = 'ducati'

# 1. Removendo pelo valor da variável muito_cara
# O Python buscará o texto 'ducati' na lista e removerá o item encontrado.
print('----- REMOVENDO A DUCATI -----')
motocicletas.remove(muito_cara)
print(motocicletas)  # A lista resultante não contém mais 'ducati'

# Exibindo o motivo da remoção
print("\n----- MOTIVO -----")
print(
    f"Após consultas foi decidido que a {muito_cara.title()} "
    "fica acima do preço!")

# ==========================================
# IMPORTANTE PARA OS ALUNOS:
# O método remove() apaga APENAS A PRIMEIRA ocorrência do valor na lista.
# Se tivéssemos duas motocicletas 'ducati' na lista, apenas a primeira seria
# apagada. Para remover todas, precisaríamos usar um laço de repetição (loop),
# assunto que será visto nos próximos capítulos.
# ==========================================

