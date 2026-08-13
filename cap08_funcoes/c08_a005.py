# CONCEITO: Argumentos Nomeados (Keyword Arguments)
# --------------------------------------------------
# Um argumento nomeado é um par 'nome=valor' passado na chamada da função.
# Ao explicitar o nome do parâmetro na chamada, a ordem em que passamos 
# os argumentos deixa de importar, evitando erros de posição!

# Definição da função com dois parâmetros: 'tipo_animal' e 'nome_pet'
def descreva_animal(tipo_animal, nome_pet):
    """Exibe informações sobre um animal."""
    print(f"\nEu tenho um {tipo_animal}.")
    print(f"Meu {tipo_animal} se chama {nome_pet.title()}.")


# Chamada 1: Especificando nome do parâmetro = valor
# 'tipo_animal' recebe 'hamster', 'nome_pet' recebe 'harry'
descreva_animal(tipo_animal='hamster', nome_pet='harry')

# Chamada 2: Invertendo a ordem dos argumentos nomeados
# Mesmo com a ordem trocada na chamada, Python atribui os valores corretamente aos parâmetros!
descreva_animal(nome_pet='harry', tipo_animal='hamster')