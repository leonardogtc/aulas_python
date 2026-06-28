# Modificando uma lista em uma função
# -----------------------------------
# Quando passamos uma lista a uma função, ela pode ser modificada.
# Qualquer alteração feita na lista no corpo da função é permanente,
# permitindo trabalhar de modo eficiente, mesmo quando lidamos com
# grandes quantidades de dados.

'''
Considere uma empresa que cria modelos de designs submetidos pelos
usuários e que são impressos em 3D. Os designs são armazenados em umalista e,
depois de impressos, são transferidos para uma lista separada.
'''

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simula a impressão de cada design, até que não haja mais nenhum
# Transfere cada design para completed_models após a impressão
while unprinted_designs:
    current_design = unprinted_designs.pop()

    # Simula a criação de uma impressão 3D a partir do design
    print("Imprimindo modelo: " + current_design)
    completed_models.append(current_design)

# Exibe todos os modelos finalizados
print("\nOs seguintes modelos foram impressos:")
for completed_model in completed_models:
    print(completed_model)
