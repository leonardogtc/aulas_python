'''
QUADRADO PERFEITO
Por exemplo, considere como criaríamos uma lista dos dez primeiros
quadrados perfeitos (isto é, o quadrado de cada inteiro de 1 a 10).
Em Python, dois asteriscos (**) representam exponenciais.
'''
squares = []
for value in range(1, 11):
    squares.append(value**2)


print(squares)
