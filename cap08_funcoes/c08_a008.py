# CONCEITO: Valores de Retorno (return)
# ------------------------------------
# Uma função nem sempre precisa apenas imprimir algo na tela (print).
# Ela pode processar dados e RETORNAR um valor para quem a chamou usando a instrução 'return'.
# O valor devolvido pode ser armazenado em uma variável ou utilizado em outras expressões.

# Definição da função que recebe dois parâmetros: 'nome' e 'sobrenome'
def nome_completo(nome, sobrenome):
    """Devolve um nome completo formatado de modo elegante."""
    # Junta nome e sobrenome intercalados por um espaço numa string
    nome_completo = f"{nome} {sobrenome}"
    # Aplica o método .title() para deixar as iniciais maiúsculas e envia o resultado de volta
    return nome_completo.title()


# Chamamos a função com 'jimi' e 'hendrix'.
# O valor retornado ("Jimi Hendrix") é atribuído/armazenado na variável 'musico'.
musico = nome_completo('jimi', 'hendrix')

# Imprimimos na tela o valor que foi retornado pela função e guardado em 'musico'
print(musico)  # Saída: Jimi Hendrix
