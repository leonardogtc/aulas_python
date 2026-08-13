# CONCEITO: Valores Default (Padrão) para Parâmetros
# ---------------------------------------------------
# Ao definir uma função, podemos atribuir um valor default a um parâmetro (ex: tipo_animal='cachorro').
# Se a chamada fornecer um valor para esse parâmetro, o Python usa o valor fornecido.
# Se a chamada omitir esse argumento, o Python usará automaticamente o valor default.
# REGRA IMPORTANTE: Parâmetros com valor default devem sempre vir APÓS os parâmetros sem valor default na definição.

# Definição da função: 'nome_pet' é obrigatório; 'tipo_animal' assume 'cachorro' por padrão se não informado.
def descreva_animal(nome_pet, tipo_animal='cachorro'):
    """Exibe informações sobre um animal."""
    print(f"\nEu tenho um {tipo_animal}.")
    print(f"Meu {tipo_animal} se chama {nome_pet.title()}.")


# Chamada 1: Usando argumento nomeado para 'nome_pet'. 'tipo_animal' assume o default 'cachorro'.
descreva_animal(nome_pet='Banana')

# Chamada 2: Usando argumento posicional. 'Banana' é associado a 'nome_pet'. 'tipo_animal' assume 'cachorro'.
descreva_animal('Banana')

# Chamada 3: Sobrescrevendo o valor default. Passamos 'hamster' para 'tipo_animal', ignorando o valor default 'cachorro'.
descreva_animal(nome_pet='harry', tipo_animal='hamster')
