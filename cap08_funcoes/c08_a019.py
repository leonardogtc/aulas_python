

def fazer_pizza(*coberturas):
    """ Exibe uma lista de ingredientes pedidos """
    for cobertura in coberturas:
        print(f" - {cobertura.title()}")

fazer_pizza('cogumelos', 'pimentões verdes', 'queijo extra')