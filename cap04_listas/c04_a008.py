'''
COPIANDO LISTAS
---------------
Com frequência, você vai querer começar com uma lista existente e criar
uma lista totalmente nova com base na primeira.
Para copiar uma lista, podemos criar uma fatia que inclua a lista original
inteira omitindo o primeiro e o segundo índices ([:]).
'''

minhas_comidas = ['pizza', 'falafel', 'carne','canelonni','porpeta']
comidas_favoritas = minhas_comidas[:]

print("Minhas comidas são:")

print(comidas_favoritas)

print("\nAs comidas favoritas são:")
print(comidas_favoritas)

# Adicionar 3 elementos na lista
comidas_favoritas.append('sorvete')

print("\nMinhas comidas agora incluem:")
print(minhas_comidas)

print("\nAs comidas favoritas agora incluem:")
print(comidas_favoritas)

