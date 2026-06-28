# Argumento nomeado com valor DEFAULT
# -----------------------------------
# Ao escrever uma função, podemos definir um valor default (padrão) para
# um ou mais parâmetros. Se um argumento for fornecido na chamada da função,
# o Python utilizará o valor do argumento. Caso contrário, utilizará o valor default.

def descreva_animal(nome_pet, tipo_animal='cachorro'):
    """Exibe informações sobre um animal."""
    print(f"\nEu tenho um {tipo_animal}.")
    print(f"Meu {tipo_animal} se chama {nome_pet.title()}.")


# Uma chamada simples que utiliza o valor default 'cachorro'
descreva_animal(nome_pet='Banana')

# Uma chamada posicional equivalente que também utiliza o valor default
descreva_animal('Banana')

# Uma chamada que sobrescreve o valor default de tipo_animal
descreva_animal(nome_pet='harry', tipo_animal='hamster')
