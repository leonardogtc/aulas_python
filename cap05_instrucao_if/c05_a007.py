'''
Testando várias condições
A cadeia if-elif-else é eficaz, mas é apropriada somente quando você
quiser que apenas um teste passe. Assim que encontrar um teste que passe,
o interpretador Python ignorará o restante dos testes. Esse comportamento
é vantajoso, pois é eficiente e permite testar uma condição específica.
Às vezes, porém, é importante verificar todas as condições de interesse.
'''

coberturas = ['pepperoni', 'cogumelos', 'mussarela extra']

if 'cogumelos' in coberturas:
    print("Adicionando cogumelos.")

if 'pepperoni' in coberturas:
    print("Adicionando pepperoni.")

if 'mussarela extra' in coberturas:
    print("Adicionando mussarela extra.")

print("\nPizza concluída!")
