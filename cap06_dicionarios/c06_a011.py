'''
UMA LISTA EM UM DICIONÁRIO
--------------------------
Em vez de colocar um dicionário em uma lista, às vezes é conveniente
colocar uma lista em um dicionário.
'''
pizza = {
    'crosta': 'espessa',
    'coberturas': ['cogumelos', 'queijo extra']
}

# Reume o pedido
print(f"Sua pizza de crosta {pizza['crosta']} com as seguintes coberturas: ")

for cobertura in pizza['coberturas']:
    print("\t" + cobertura)
