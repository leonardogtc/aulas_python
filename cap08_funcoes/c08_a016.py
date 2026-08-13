# CONCEITO: Preservando a Lista Original Enviando uma Cópia [:]
# -----------------------------------------------------------
# Para evitar que uma função altere a lista original, podemos passar uma CÓPIA em vez da lista original.
# Usamos a notação de fatiamento `lista[:]` que gera uma cópia superficial (shallow copy) da lista.

# Função 1: Altera a lista que recebe no primeiro parâmetro
def print_models(unprinted_designs, completed_models):
    """
    Simula a impressão de cada design, transferindo de unprinted_designs para completed_models.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)


# Função 2: Exibe os modelos concluídos
def show_completed_models(completed_models):
    """Mostra todos os modelos impressos."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


# --- CÓDIGO PRINCIPAL ---

# Lista original de designs
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']

# Lista vazia para modelos impressos
completed_models = []

# PONTO CHAVE: Passamos 'unprinted_designs[:]' (uma cópia).
# A função 'print_models' vai esvaziar a CÓPIA, mas a lista original 'unprinted_designs' permanecerá intacta!
print_models(unprinted_designs[:], completed_models)

# Exibimos a lista original no terminal para comprovar que seus itens NÃO foram removidos
print("\nLista original preservada:", unprinted_designs)

# Exibimos os modelos concluídos acumulados na lista completed_models
show_completed_models(completed_models)