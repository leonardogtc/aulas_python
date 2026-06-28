# Argumentos --> São valores passados para a função.
# Argumentos posicionais
# ----------------------
# Quando chamamos uma função, Python precisa fazer a correspondência
# entre cada argumento da chamada da função e um parâmetro da definição.
# A maneira mais simples de fazer isso é contar com a ordem dos argumentos
# fornecidos. Valores cuja correspondência seja feita dessa maneira são
# chamados de argumentos posicionais.

def descreva_animal(tipo, nome):
    """Exibe informações sobre um animal."""
    print(f"\nEu tenho um {tipo}.")
    print(f"Meu {tipo} se chama {nome.title()}.")


descreva_animal('hamster', 'harry')

# Várias chamadas de função
# -------------------------
# Podemos chamar uma função quantas vezes forem necessárias. Descrever
# um segundo animal de estimação diferente exige apenas mais uma
# chamada a descreva_animal():

descreva_animal('cachorro', 'Banana')

# Chamar uma função várias vezes é uma maneira eficiente de trabalhar.
# A ordem é importante em argumentos posicionais