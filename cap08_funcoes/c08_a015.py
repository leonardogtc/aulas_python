# CONCEITO: Modularização com Funções Mutáveis
# ---------------------------------------------
# Organizar o código em funções separadas torna o programa mais limpo, fácil de ler e reutilizável.
# Aqui, dividimos o problema em duas tarefas distintas:
# 1. Processar/imprimir os modelos (`print_models`).
# 2. Exibir o resultado final (`show_completed_models`).
# Como passamos a lista 'unprinted_designs' diretamente, a função MODIFICA a lista original!

# Função 1: Responsável por simular o processo de impressão e atualizar as listas
def print_models(unprinted_designs, completed_models):
    """
    Simula a impressão de cada design, até que não haja mais nenhum na lista pendente.
    Transfere cada design para completed_models após a impressão.
    """
    # Enquanto a lista unprinted_designs tiver elementos (avaliada como True)
    while unprinted_designs:
        # Remove o último item de unprinted_designs (LIFO - Last In, First Out)
        current_design = unprinted_designs.pop()

        # Exibe mensagem simulando a impressão do modelo atual
        print("Printing model: " + current_design)

        # Adiciona o modelo impresso no final da lista completed_models
        completed_models.append(current_design)


# Função 2: Responsável apenas por exibir a lista de modelos que foram impressos
def show_completed_models(completed_models):
    """Mostra todos os modelos impressos."""
    print("\nThe following models have been printed:")
    # Percorre a lista de modelos concluídos e imprime cada um
    for completed_model in completed_models:
        print(completed_model)


# --- CÓDIGO PRINCIPAL (MAIN PROGRAM) ---

# Declara a lista original de designs pendentes
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']

# Declara a lista vazia para armazenar modelos concluídos
completed_models = []

# Chamada da 1ª função: realiza a transferência de itens de unprinted_designs para completed_models
print_models(unprinted_designs, completed_models)

# Chamada da 2ª função: exibe a lista final com todos os modelos concluídos
show_completed_models(completed_models)

# NOTA PARA O ALUNO: Após a execução da função 'print_models', a lista 'unprinted_designs' fica VAZIA ([]).
