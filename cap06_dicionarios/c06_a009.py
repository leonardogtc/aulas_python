'''
INFORMAÇÕES ANINHADAS
---------------------
Às vezes, você vai querer armazenar um conjunto de dicionários em uma
lista ou uma lista de itens como um valor em um dicionário. Isso é
conhecido como aninhar informações. Podemos aninhar um conjunto de
dicionários em uma lista, uma lista de itens em um dicionário ou até
mesmo um dicionário em outro dicionário. Aninhar informações é um
recurso eficaz, como mostrarão os próximos exemplos.
'''

alien_0 = {'cor': 'verde', 'pontos': 5}
alien_1 = {'cor': 'verde', 'pontos': 15}
alien_2 = {'cor': 'verde', 'pontos': 10}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
