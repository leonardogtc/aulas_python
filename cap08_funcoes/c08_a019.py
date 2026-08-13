# CONCEITO: Iterando sobre Tupla de Argumentos Arbitrários (*coberturas)
# ---------------------------------------------------------------------
# Como o parâmetro '*coberturas' empacota os argumentos em uma TUPLA, 
# podemos usar um laço 'for' para percorrer e formatar cada item individualmente.

def fazer_pizza(*coberturas):
    """Exibe um resumo dos ingredientes pedidos para a pizza."""
    print("\nPreparando uma pizza com os seguintes ingredientes:")
    # O laço 'for' itera por cada elemento presente na tupla 'coberturas'
    for cobertura in coberturas:
        # Formata o ingrediente com marcador e inicial maiúscula
        print(f" - {cobertura.title()}")


# Chamada de teste passando 3 coberturas
fazer_pizza('cogumelos', 'pimentões verdes', 'queijo extra')
