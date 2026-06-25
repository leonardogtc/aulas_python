'''
Com frequência, suas listas serão criadas em uma ordem imprevisível, pois
nem sempre você poderá controlar a ordem em que seus usuários fornecem
seus dados. Embora isso seja inevitável na maioria das circunstâncias, com
frequência você vai querer apresentar suas informações em uma ordem em
particular.
'''
carros = ['bmw', 'audi', 'toyota', 'subaru']
print(carros)

# Ordenando com sort()
# OBS: O método sort() altera a ordem da lista de forma permanente.
carros.sort()
print(carros)

# Podemos ordenar essa lista em ordem alfabética inversa, passando
# o argumento reverse=True ao método sort().
carros.sort(reverse=True)
print(carros)

# Ordenando de maneira temporária com o método sorted()
carros = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(carros))
