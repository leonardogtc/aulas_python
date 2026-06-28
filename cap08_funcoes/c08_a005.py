# Argumentos Nomeados
# -------------------
# Um argumento nomeado (keyword argument) é um par nome-valor
# passado para uma função. Associamos diretamente o nome e o valor no
# próprio argumento para que não haja confusão quando ele for passado
# para a função.

def descreva_animal(tipo_animal, nome_pet):
    """Exibe informações sobre um animal."""
    print(f"\nEu tenho um {tipo_animal}.")
    print(f"Meu {tipo_animal} se chama {nome_pet.title()}.")


descreva_animal(tipo_animal='hamster', nome_pet='harry')
descreva_animal(nome_pet='harry', tipo_animal='hamster')