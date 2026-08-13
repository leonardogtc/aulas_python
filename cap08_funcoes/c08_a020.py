# CONCEITO: Misturando Argumentos Posicionais e Arbitrários
# --------------------------------------------------------
# REGRA DE OURO: Se uma função precisar receber argumentos posicionais normais E argumentos arbitrários (*args),
# o parâmetro que aceita número arbitrário de argumentos MUST BE / DEVE SER colocado por ÚLTIMO na definição!

# 1º parâmetro: 'tamanho' -> captura obrigatoriamente o 1º argumento posicional.
# 2º parâmetro: '*coberturas' -> captura TODOS os argumentos adicionais em uma tupla.
def pizza(tamanho, *coberturas):
    """Apresenta a pizza que estamos prestes a preparar!"""
    print(f"\nFazendo uma pizza de tamanho {tamanho}.")
    print("Com as seguintes coberturas:")
    for cobertura in coberturas:
        print(f" - {cobertura.title()}")


# Na chamada:
# 'familía' -> vai para 'tamanho'
# 'cogumelos', 'pimentões verdes', 'queijo extra' -> são agrupados na tupla '*coberturas'
pizza('familía', 'cogumelos', 'pimentões verdes', 'queijo extra')
