'''
Nota: Às vezes, você vai querer usar o valor de um item depois de removê-lo de
uma lista. Por exemplo, talvez você queira obter as posições x e y de um
alienígena que acabou de ser atingido para que possa desenhar uma explosão
nessa posição. Em uma aplicação web, você poderia remover um usuário de uma
lista de membros ativos e então adicioná-lo a uma lista de membros inativos.

O método pop() remove o último item de uma lista, mas permite que você
trabalhe com esse item depois da remoção.
'''
motocicletas = ['honda', 'yamaha', 'suzuki', 'ducati', 'kawazaki']
print(motocicletas)

# Removendo e armazenando o último item
moto_removida = motocicletas.pop()
print(motocicletas)
print(f"A motocicleta removida foi a {moto_removida.title()}.")

# Removendo e armazenando qualquer motocicleta
print(f"Motocicletas restantes: {motocicletas}")

# Removendo Yamaha:
print("----- Removendo yamaha ----- ")
moto_removida = motocicletas.pop(1)
print(f"A motocicleta removida foi a {moto_removida.title()}.")
print(f"Motocicletas restantes: {motocicletas}")
