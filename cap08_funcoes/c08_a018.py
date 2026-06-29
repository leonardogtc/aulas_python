# Passando um número arbitrário de argumentos
# O asterisco no nome do parâmetro *toppings diz a Python para criar uma
# tupla vazia chamada toppings e reunir os valores recebidos nessa tupla.

def fazer_pizza(*coberturas):
    """ Exibe uma lista de ingredientes pedidos """
    print(coberturas)


fazer_pizza('peperoni')
fazer_pizza('cogumelos', 'pimentões verdes', 'queijo extra')
