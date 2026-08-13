# CONCEITO: Integrando Funções com Laços de Repetição (while)
# -----------------------------------------------------------
# É muito comum usar funções dentro de laços de repetição (como 'while') 
# para processar dados de entrada obtidos dinamicamente do usuário (input).

# Função auxiliar dedicada exclusivamente a formatar o nome completo
def get_nome_completo(nome, sobrenome):
    """Devolve um nome completo formatado de modo elegante."""
    nome_completo = f"{nome.title()} {sobrenome.title()}"
    return nome_completo


# Laço infinito 'while True' para manter o programa rodando até o usuário decidir sair
while True:
    print("\nDigite o seu nome: ")
    print("Digite 'q' para sair a qualquer momento!")

    # Solicita a entrada do nome
    nome = input("Nome: ")

    # Condição de saída: se o usuário digitar 'q', encerra o laço com 'break'
    if nome == 'q':
        break

    # Solicita a entrada do sobrenome
    sobrenome = input("Sobrenome: ")

    # Condição de saída alternativa caso o usuário queira sair após digitar o primeiro nome
    if sobrenome == 'q':
        break

    # Chama a função enviando os dados digitados e recebe o nome formatado
    nome_completo = get_nome_completo(nome, sobrenome)
    
    # Exibe a saudação final com o nome retornado pela função
    print(f"Olá, {nome_completo}")