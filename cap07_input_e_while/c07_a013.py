'''
Evitando loops infinitos
------------------------
Todo laço while precisa de uma maneira de interromper a execução para
que não continue executando indefinidamente.
'''
x = 1
while x <= 5:
    print(x)
    x += 1 # Se for omitido um laço infinito será criado!

