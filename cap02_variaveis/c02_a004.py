# Variáveis
# ---------

# - tipos por inferência
numero = 2
print(numero)
print(type(numero))

# Variável global
if numero > 2:
    novo = numero + 10
    print(novo)


print(novo)  # Erro, pois a variável novo não é global
