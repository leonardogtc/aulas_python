# Tipo String

nome = 'Leonardo Gonçalves Tavares da Conceição'

print(nome.upper())
print(nome.lower())
print(type(nome))
print(nome.split())     # Separa os nomes em uma lista
print(list(nome))       # Coloca cada caracter em uma posição da lista

lst_nome = nome.split()
print(lst_nome[0].split())

empresa = 'GEEK UNIVERSITY'
print(empresa.split())
print(list(empresa))

# Pegar o primeiro nome e inverter os caracteres
print(list(nome.split()[0])[::-1])

# Replace
print(list((nome.split()[0].replace('o', 'x').replace('L','l')).lower().title())[::-1])
