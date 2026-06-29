# Misturando argumentos posicionais e arbitrários
# -----------------------------------------------
'''
o parâmetro que aceita um número arbitrário de
argumentos deve ser colocado por último na definição
da função.
'''


def pizza(tamanho, *coberturas):
    """ Apresenta a pizza que estamos prestes a preparar! """
    print(f"\nFazendo uma pizza {tamanho}.")
    print(f"Com as seguintes coberturas:")
    for cobertura in coberturas:
        print(f" - {cobertura.title()}")


pizza('familía', 'cogumelos', 'pimentões verdes', 'queijo extra')