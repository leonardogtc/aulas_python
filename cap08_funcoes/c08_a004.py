# CONCEITO: Argumentos Posicionais
# -----------------------------
# Argumentos --> São valores passados para a função no momento em que ela é chamada.
# Argumentos posicionais: Python associa cada argumento na chamada a um parâmetro
# na definição com base estritamente na ORDEM em que foram escritos.

# Definimos a função 'descreva_animal' com dois parâmetros: 'tipo' (primeiro) e 'nome' (segundo)
def descreva_animal(tipo, nome):
    """Exibe informações sobre um animal de estimação."""
    # Exibe o tipo de animal recebido
    print(f"\nEu tenho um {tipo}.")
    # Exibe o nome do animal formatado com a primeira letra maiúscula através de .title()
    print(f"Meu {tipo} se chama {nome.title()}.")


# Primeira chamada usando argumentos posicionais:
# 'hamster' é o 1º argumento -> vai para o parâmetro 'tipo'
# 'harry' é o 2º argumento   -> vai para o parâmetro 'nome'
descreva_animal('hamster', 'harry')


# Várias chamadas de função
# -------------------------
# Podemos reutilizar o mesmo código chamando a função com novos valores:
# 'cachorro' é o 1º argumento -> vai para 'tipo'
# 'Banana' é o 2º argumento   -> vai para 'nome'
descreva_animal('cachorro', 'Banana')

# ATENÇÃO ALUNO: Em argumentos posicionais, inverter a ordem dos argumentos
# alterará o resultado ou causará inconsistências (ex: descreva_animal('harry', 'hamster')).