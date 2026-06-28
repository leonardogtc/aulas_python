# Deixando um argumento opcional
# Nota: Valores default podem ser usados para deixar um argumento opcional.
# Para que funcione, definimos o nome_do_meio como vazio e passamos o argu-
# mento para o final.

def nome_completo(nome, sobrenome, nome_do_meio=''):
    """ Devolve o nome completo formato de maneira elegante."""
    if nome_do_meio:
        nome_completo = f"{nome} {nome_do_meio} {sobrenome}"
    else:
        nome_completo = f"{nome} {sobrenome}"

    return nome_completo


pessoa = nome_completo('Leonardo', 'Conceição')
print(pessoa)

pessoa1 = nome_completo('Oliver', 'Conceição', 'Pontes Tavares')
print(pessoa1)
