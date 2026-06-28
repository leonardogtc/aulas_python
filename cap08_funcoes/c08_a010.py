# Devolvendo um dicionário
# Uma função pode devolver qualquer tipo de valor necessário, incluindo
# estruturas de dados mais complexas como listas e dicionários.

def criando_pessoa(nome, sobrenome, idade=''):
    """ Devolve um dicionário com informações sobre uma pessoa. """
    if idade:
        pessoa = {
            'nome': nome,
            'sobrenome': sobrenome,
            'idade': idade,
        }
    else:
        pessoa = {
            'nome': nome,
            'sobrenome': sobrenome,
        }
    return pessoa


pessoa = criando_pessoa('Oliver', 'Conceição')
print(pessoa)

pessoa1 = criando_pessoa('Leonardo', 'Conceição', 56)
print(pessoa1)
