'''
EXERCÍCIOS 8.3, 8.4 e 8.5

8.3 – Camiseta: Escreva uma função chamada make_shirt() que aceite um
tamanho e o texto de uma mensagem que deverá ser estampada na camiseta. A
função deve exibir uma frase que mostre o tamanho da camiseta e a mensagem
estampada.
Chame a função uma vez usando argumentos posicionais para criar uma
camiseta. Chame a função uma segunda vez usando argumentos nomeados.

8.4 – Camisetas grandes: Modifique a função make_shirt() de modo que as
camisetas sejam grandes por default, com uma mensagem Eu amo Python. Crie
uma camiseta grande e outra média com a mensagem default, e uma camiseta de
qualquer tamanho com uma mensagem diferente.

8.5 – Cidades: Escreva uma função chamada describe_city() que aceite o
nome de uma cidade e seu país. A função deve exibir uma frase simples, como
Reykjavik está localizada na Islândia. Forneça um valor default ao
parâmetro que representa o país. Chame sua função para três cidades diferentes
em que pelo menos uma delas não esteja no país default.
'''

# --- EXERCÍCIO 8.3 ---
print("--- Exercício 8.3 ---")
# Função básica com dois parâmetros posicionais: tamanho e texto_mensagem
def make_shirt(tamanho, texto_mensagem):
    """Exibe o tamanho e a mensagem a ser impressa na camiseta."""
    print(f"Camiseta tamanho '{tamanho}' estampada com: \"{texto_mensagem}\"")

# Chamada 1: Usando argumentos posicionais (a ordem importa!)
make_shirt('G', 'Python é incrível!')

# Chamada 2: Usando argumentos nomeados (a ordem não importa)
make_shirt(texto_mensagem='Código Limpo', tamanho='M')


# --- EXERCÍCIO 8.4 ---
print("\n--- Exercício 8.4 ---")
# Modificação com valores default: tamanho='G' e texto_mensagem='Eu amo Python'
def make_shirt_default(tamanho='G', texto_mensagem='Eu amo Python'):
    """Exibe informações da camiseta com valores default para tamanho G e mensagem 'Eu amo Python'."""
    print(f"Camiseta tamanho '{tamanho}' estampada com: \"{texto_mensagem}\"")

# 1. Camiseta grande (default) com mensagem default
make_shirt_default()

# 2. Camiseta média com mensagem default (sobrescrevendo apenas o tamanho)
make_shirt_default(tamanho='M')

# 3. Camiseta de qualquer tamanho (P) com uma mensagem diferente
make_shirt_default(tamanho='P', texto_mensagem='Aprender é divertido!')


# --- EXERCÍCIO 8.5 ---
print("\n--- Exercício 8.5 ---")
# Função describe_city com parâmetro pais tendo valor default 'Brasil'
def describe_city(cidade, pais='Brasil'):
    """Exibe uma frase informando a cidade e seu país."""
    print(f"{cidade.title()} está localizada no(a) {pais.title()}.")

# Chamada 1: Usando o país default (Brasil)
describe_city('São Paulo')

# Chamada 2: Outra cidade usando o país default (Brasil)
describe_city('Rio de Janeiro')

# Chamada 3: Sobrescrevendo o país default
describe_city('Tóquio', 'Japão')