'''
EXERCÍCIOS 8.12, 8.13 e 8.14

8.12 – Sanduíches: Escreva uma função que aceite uma lista de itens que uma
pessoa quer em um sanduíche. A função deve ter um parâmetro que agrupe tantos
itens quantos forem fornecidos pela chamada da função e deve apresentar um
resumo do sanduíche pedido. Chame a função três vezes.

8.13 – Perfil do usuário: Crie um perfil seu chamando build_profile(), usando 
seu primeiro nome e o sobrenome, além de três outros pares chave-valor.

8.14 – Carros: Escreva uma função que armazene informações sobre um carro em
um dicionário. A função sempre deve receber o nome de um fabricante e um
modelo, além de um número arbitrário de argumentos nomeados (**kwargs).
'''

# --- EXERCÍCIO 8.12 ---
print("--- Exercício 8.12 ---")
def sanduiche(*itens):
    """Exibe um resumo dos ingredientes escolhidos para o sanduíche."""
    print("\nFazendo um sanduíche com os seguintes itens:")
    for item in itens:
        print(f" - {item}")

# Chamadas testando quantidades variáveis de ingredientes
sanduiche('queijo', 'presunto')
sanduiche('alface', 'tomate', 'pimenta malagueta', 'frango desfiado')
sanduiche('hambúrguer gourmet', 'bacon', 'cheddar', 'cebola caramelizada')


# --- EXERCÍCIO 8.13 ---
print("\n--- Exercício 8.13 ---")
def build_profile(primeiro, ultimo, **user_info):
    """Constrói um dicionário com os dados do usuário."""
    profile = {
        'primeiro_nome': primeiro,
        'sobrenome': ultimo
    }
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Criando o perfil com 3 pares chave-valor adicionais
meu_perfil = build_profile(
    'Leonardo', 'Conceição',
    profissao='Desenvolvedor / Instrutor',
    linguagem_favorita='Python',
    hobby='Música'
)
print(meu_perfil)


# --- EXERCÍCIO 8.14 ---
print("\n--- Exercício 8.14 ---")
def make_car(fabricante, modelo, **car_info):
    """Constrói um dicionário contendo todas as informações sobre um automóvel."""
    carro = {
        'fabricante': fabricante.title(),
        'modelo': modelo.title()
    }
    # Adiciona todos os argumentos nomeados adicionais passados ao dicionário
    for key, value in car_info.items():
        carro[key] = value
    return carro

# Chamada conforme especificado no enunciado do livro
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
