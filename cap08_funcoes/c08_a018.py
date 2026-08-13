# CONCEITO: Número Arbitrário de Argumentos Posicionais (*args)
# -------------------------------------------------------------
# O caractere asterisco (*) antes do nome do parâmetro (ex: *coberturas) indica que
# a função pode receber ZERO ou NÚMEROS ILIMITADOS de argumentos posicionais.
# O Python junta todos os valores passados em uma TUPLA imutável chamada 'coberturas'.

# Definição da função aceitando quantidade variável de coberturas
def fazer_pizza(*coberturas):
    """Exibe a tupla com todos os ingredientes recebidos."""
    # Imprime diretamente a tupla gerada pelo Python
    print(coberturas)


# Chamada 1: Passando 1 único argumento -> resulta na tupla ('peperoni',)
fazer_pizza('peperoni')

# Chamada 2: Passando 3 argumentos -> resulta na tupla ('cogumelos', 'pimentões verdes', 'queijo extra')
fazer_pizza('cogumelos', 'pimentões verdes', 'queijo extra')
