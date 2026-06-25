"""
Usando continue em um laço
--------------------------
Em vez de sair totalmente de um laço sem executar o restante de seu
código, podemos usar a instrução continue para retornar ao início, com
base no resultado de um teste condicional.
"""

numero_atual = 0
while numero_atual < 10:
    numero_atual += 1
    if numero_atual % 2 == 0:
        continue

    print(numero_atual)