# ==========================================
# Removendo e Recuperando Itens com .pop()
# O método pop() remove um item da lista, mas nos
# retorna (devolve) esse valor para que possamos guardá-lo
# em uma variável e usá-lo depois.
# ==========================================

# NOTA DIDÁTICA:
# Pense na lista como uma pilha. O termo "pop" vem de "desempilhar" (tirar do topo/fim).
# - del: Deleta e "esquece" o item.
# - pop(): Remove e "devolve" o item para você usar.

# Lista inicial com 5 elementos
motocicletas = ['honda', 'yamaha', 'suzuki', 'ducati', 'kawazaki']
print(motocicletas)

# 1. Removendo e armazenando o último item (sem especificar índice)
# Chamar pop() vazio remove o último item ('kawazaki') e o guarda em 'moto_removida'.
moto_removida = motocicletas.pop()
print(motocicletas)  # A lista agora não tem mais 'kawazaki'
print(f"A motocicleta removida foi a {moto_removida.title()}.")

# Exibindo as motocicletas que sobraram na lista
print(f"Motocicletas restantes: {motocicletas}")

# 2. Removendo e armazenando um item de qualquer posição
# Podemos passar o índice como argumento para o pop(indice).
# pop(1) remove a 'yamaha' (índice 1) e a guarda na variável 'moto_removida'.
print("----- Removendo yamaha ----- ")
moto_removida = motocicletas.pop(1)
print(f"A motocicleta removida foi a {moto_removida.title()}.")
print(f"Motocicletas restantes: {motocicletas}")

