'''
- Você pode remover um item de qualquer posição em uma lista usando a
instrução del, se souber qual é o seu índice.

del.motocicletas[1]

'''
motocicletas = ['honda', 'yamaha', 'suzuki', 'ducati', 'kawazaki']
print(motocicletas)

# Apagando elemento na 4ª posição
del motocicletas[4]
print(motocicletas)

# Apagando o último elemento com del [-1]
del motocicletas[-1]
print(motocicletas)
