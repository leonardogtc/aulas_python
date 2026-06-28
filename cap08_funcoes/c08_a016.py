'''
Evitando que uma função modifique uma lista
-------------------------------------------
Às vezes, você vai querer evitar que uma função modifique uma lista.

Você pode enviar uma cópia de uma lista para uma função assim:

nome_da_função(nome_da_lista[:])

A notação de fatia [:] cria uma cópia da lista para ser enviada à função.

'''

def print_models(unprinted_designs, completed_models):
    """
    Simula a impressão de cada design, até que não haja mais nenhum.
    Transfere cada design para completed_models após a impressão.
    """
    # Loop continua enquanto houver itens na lista de designs pendentes (unprinted_designs)
    while unprinted_designs:
        # Remove o último item da lista unprinted_designs (LIFO - Last In, First Out)
        current_design = unprinted_designs.pop()

        # Simula a criação de uma impressão 3D a partir do design
        print("Printing model: " + current_design)
        
        # Adiciona o design que acabou de ser impresso à lista de modelos concluídos
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Mostra todos os modelos impressos."""
    print("\nThe following models have been printed:")
    # Percorre a lista de modelos concluídos e exibe cada um deles
    for completed_model in completed_models:
        print(completed_model)


# Lista inicial contendo os designs que precisam ser impressos
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']

# Lista vazia que será preenchida com os modelos conforme forem impressos
completed_models = []

# Executa a função para simular a impressão dos designs
print_models(unprinted_designs[:], completed_models)

# Lista continua a mesma - foi feita alteração em uma cópia
print(unprinted_designs)

# Executa a função para exibir a lista final de modelos impressos
show_completed_models(completed_models)