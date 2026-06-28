# Devolvendo um valor simples
# ---------------------------
# Uma função nem sempre precisa exibir sua saída diretamente. Em vez
# disso, ela pode processar alguns dados e então devolver um valor ou um
# conjunto de valores. O valor devolvido pela função é chamado de valor de
# retorno. A instrução return toma um valor que está em uma função e o
# envia de volta à linha que a chamou.

def nome_completo(nome, sobrenome):
    """Devolve um nome completo formatado de modo elegante."""
    nome_completo = f"{nome} {sobrenome}"
    return nome_completo.title()


musico = nome_completo('jimi', 'hendrix')
print(musico)
