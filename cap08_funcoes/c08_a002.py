'''
CONCEITO: Passando Informação para a Função (Parâmetros e Argumentos)
-------------------------------------------------------------------
- Parâmetro: variável declarada na definição da função (ex: username).
- Argumento: valor real passado para a função no momento da chamada (ex: "Leonardo").
'''

# Definimos a função 'saudacao' declarando 'username' entre os parênteses.
# 'username' atua como um parâmetro (uma variável local que receberá um valor).
def saudacao(username):
    """Exibe uma saudação simples personalizada."""  # Docstring descrevendo a função
    # Utiliza f-string para formatar o texto inserindo o valor armazenado na variável 'username'
    print(f'Olá! {username}.')


# Chamamos a função 'saudacao' passando a string "Leonardo" como argumento.
# Python atribui o valor "Leonardo" ao parâmetro 'username' e executa o bloco interno.
saudacao("Leonardo")  # Imprime: Olá! Leonardo.