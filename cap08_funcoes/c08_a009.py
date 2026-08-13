# CONCEITO: Parâmetros Opcionais com Valores Default Vazios
# --------------------------------------------------------
# Podemos deixar um parâmetro opcional atribuindo a ele uma string vazia '' como valor default.
# Na linguagem Python, uma string vazia '' é avaliada como Falsa em um teste lógico 'if'.
# Se um texto for fornecido, a string não será vazia e será avaliada como Verdadeira (True).

# 'nome_do_meio' é posicionado por último e recebe '' como padrão (opcional)
def nome_completo(nome, sobrenome, nome_do_meio=''):
    """Devolve o nome completo formatado de maneira elegante."""
    # Se 'nome_do_meio' contiver algum texto (não for vazio ''), o bloco 'if' é executado
    if nome_do_meio:
        nome_completo = f"{nome} {nome_do_meio} {sobrenome}"
    # Caso contrário (se 'nome_do_meio' for ''), executa o bloco 'else'
    else:
        nome_completo = f"{nome} {sobrenome}"

    # Retorna a string formatada
    return nome_completo


# Chamada sem o argumento opcional 'nome_do_meio'
pessoa = nome_completo('Leonardo', 'Conceição')
print(pessoa)  # Imprime: Leonardo Conceição

# Chamada fornecendo o argumento opcional 'nome_do_meio'
pessoa1 = nome_completo('Oliver', 'Conceição', 'Pontes Tavares')
print(pessoa1)  # Imprime: Oliver Pontes Tavares Conceição
