# Usando uma função com um laço while

def get_nome_completo(nome, sobrenome):
    """ Devolve um nome completo formatado de modo elegante """
    nome_completo = f"{nome.title()} {sobrenome.title()}"
    return nome_completo


while True:
    print("\nDigite o seu nome: ")
    print("Digite 'q' para sair a qualquer momento!")

    nome = input("Nome: ")

    if nome == 'q':
        break

    sobrenome = input("Sobrenome: ")

    if sobrenome == 'q':
        break

    nome_completo = get_nome_completo(nome, sobrenome)
    print(f"Olá, {nome_completo}")