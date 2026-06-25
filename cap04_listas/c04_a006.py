'''
List comprehensions

A abordagem descrita antes para gerar a lista squares usou três ou quatro
linhas de código. Uma list comprehension (abrangência de lista) permite
gerar essa mesma lista com apenas uma linha de código.

Uma list comprehension combina o laço for e a criação de novos elementos
em uma linha, e concatena cada novo elemento automaticamente.

'''

squares = [value ** 2 for value in range(1, 11)]
print(squares)

'''
Para usar essa sintaxe, comece com um nome descritivo para a lista, por
exemplo, squares. Em seguida, insira um colchete de abertura e defina a
expressão para os valores que você quer armazenar na nova lista. Nesse
exemplo, a expressão é value**2, que eleva o valor ao quadrado. Então
escreva um laço for para gerar os números que você quer fornecer à
expressão e insira um colchete de fechamento. O laço for nesse exemplo é
for value in range(1,11), que fornece os valores de 1 a 10 à expressão
value**2. Observe que não usamos dois-pontos no final da instrução for.
'''