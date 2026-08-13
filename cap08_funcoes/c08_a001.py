'''
CONCEITO: Funções e Docstrings
-----------------------------------
Funções --> são blocos de código nomeados, concebidos para realizar uma tarefa específica.
Se precisar executar essa tarefa várias vezes durante seu programa, não será necessário 
digitar todo o código para a mesma tarefa repetidamente: basta chamar a função dedicada
ao tratamento dessa tarefa.

Docstring (document string) --> é uma string literal usada para documentar uma parte do código, 
como uma função, classe ou módulo. Ela é delimitada por três aspas (duplas ou simples) e deve ser 
colocada logo na primeira linha do bloco. O interpretador Python a reconhece automaticamente e a 
associa ao atributo especial `__doc__`, que pode ser acessado programaticamente ou exibido via help().
'''

# A palavra-chave 'def' informa ao Python que estamos definindo/criando uma função.
# 'saudacao' é o nome atribuído à função. Os parênteses () indicam que ela não recebe parâmetros.
# O dois-pontos (:) inicia o bloco de código (corpo) da função, que deve ser indentado.
def saudacao():
    """Exibe uma saudação simples."""  # Docstring: explica brevemente o que esta função faz
    print('Olá!')  # Exibe a mensagem no terminal quando a função for chamada


# Chamada de função: instrução que direciona o fluxo de execução do programa para a função definida anteriormente, executando o seu bloco de código. É feita informando # o nome da função seguido por parênteses: nome_da_funcao().
saudacao()  # Executa a função 'saudacao', imprimindo 'Olá!' na tela
