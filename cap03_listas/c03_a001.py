# ==========================================
# Criação de Listas e Estruturas de Dados
# Este código demonstra diferentes formas de
# criar listas e tuplas em Python.
# ==========================================

# 1. Criando uma lista vazia usando colchetes []
# Esta é a forma mais comum e recomendada de criar uma lista vazia em Python.
motocicletas = []

# A função type() serve para descobrir qual é o tipo de dado de uma variável.
# Para "motocicletas", ela exibirá <class 'list'> (classe lista).
print(type(motocicletas))

# Exibe o conteúdo atual da lista. Como ela está vazia, o resultado na tela será []
print(motocicletas)


# 2. Criando uma lista pré-preenchida com elementos
# Criamos uma lista chamada "bicicletas" contendo três strings (textos).
# Cada elemento da lista é separado por uma vírgula.
bicicletas = ['caloi', 'monark', 'bmx']

# Exibe o tipo de dado da variável "bicicletas", que também será <class 'list'>.
print(type(bicicletas))

# Exibe os itens guardados dentro da lista: ['caloi', 'monark', 'bmx']
print(bicicletas)


# 3. Criando uma lista vazia usando a função construtora list()
# Esta é uma alternativa à sintaxe de colchetes [].
# A função list() cria uma lista vazia e é muito utilizada para conversão de outros dados em listas.
telefones = list()

# Exibe o tipo do objeto, que é <class 'list'>.
print(type(telefones))

# Exibe a lista vazia na tela: []
print(telefones)


# 4. Criando uma Tupla (Tuple)
# Atenção: criamos uma sequência de números separados apenas por vírgula.
# Em Python, se colocarmos valores separados por vírgula sem colchetes,
# o Python cria automaticamente uma Tupla (uma coleção ordenada e IMUTÁVEL).
numeros = 10, 20, 30, 40, 50

# Exibe o tipo de dado. A saída será <class 'tuple'> (classe tupla).
# Diferente da lista, os valores de uma tupla não podem ser alterados após a criação.
print(type(numeros))

# Ao exibir a tupla, o Python mostrará os elementos entre parênteses: (10, 20, 30, 40, 50)
print(numeros)
