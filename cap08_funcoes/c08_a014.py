# CONCEITO: Modificando Listas (Abordagem Sequencial / Sem Funções)
# ---------------------------------------------------------------
# Em Python, listas são objetos mutáveis. Alterações como remover (.pop) ou adicionar (.append)
# modificam a lista original na memória.
# Este arquivo demonstra a lógica de transferência de itens entre duas listas ANTES de organizá-la em funções.

# Lista inicial com os modelos pendentes de impressão 3D
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']

# Lista vazia que receberá os modelos após concluídos
completed_models = []

# O laço 'while unprinted_designs' continua executando enquanto a lista 'unprinted_designs' NÃO estiver vazia
while unprinted_designs:
    # O método .pop() remove e retorna o ÚLTIMO elemento da lista (comportamento de pilha / LIFO)
    current_design = unprinted_designs.pop()

    # Simula a impressão exibindo a mensagem no console
    print("Imprimindo modelo: " + current_design)

    # O método .append() insere o modelo impresso ao final da lista 'completed_models'
    completed_models.append(current_design)

# Exibe o relatório final de modelos impressos
print("\nOs seguintes modelos foram impressos:")

# O laço 'for' percorre a lista de modelos concluídos para exibi-los um a um
for completed_model in completed_models:
    print(completed_model)
