'''
UM DICIONÁRIO EM UM DICIONÁRIO
------------------------------
Podemos aninhar um dicionário em outro dicionário, mas o código poderá
ficar complicado rapidamente se isso for feito.
'''

# Passo 1: Definimos um dicionário chamado 'usuarios'.
# A chave é o nome de usuário (string) e o valor associado é OUTRO dicionário.
# Esse dicionário interno armazena informações detalhadas de cada usuário (nomes e localização).
usuarios = {
    'oliverptc': {
        'first_name': 'oliver',
        'middle_name': 'pontes tavares',
        'last_name': 'conceicao',
        'location': 'Feira de Santana - BA',
    },

    'luciaptc': {
        'first_name': 'lucia',
        'middle_name': 'pontes tavares',
        'last_name': 'conceicao',
        'location': 'São Francisco do Conde - BA',
    },

    'ivonete': {
        'first_name': 'ivonete',
        'middle_name': 'pontes',
        'last_name': 'cardoso',
        'location': 'São Francisco do Conde - BA',
    },

    'ayme': {
        'first_name': 'ayme',
        'middle_name': 'pontes',
        'last_name': 'cardoso',
        'location': 'São Francisco do Conde - BA',
    }
}

# Passo 2: Usamos um loop 'for' para percorrer o dicionário 'usuarios'.
# O método '.items()' retorna a chave ('username') e o valor ('user_info', que é o dicionário interno).
for username, user_info in usuarios.items():
    # Passo 3: Exibimos o nome de usuário.
    # O caractere especial '\n' insere uma quebra de linha para separar visualmente as informações de cada usuário.
    print(f"\nUsername: {username}")
    
    # Passo 4: Acessamos os dados do dicionário interno 'user_info' usando as respectivas chaves.
    # Usamos '.title()' para garantir que a primeira letra de cada nome fique em maiúscula.
    # Unimos tudo na string formatada 'full_name'.
    full_name = f"{user_info['first_name'].title()} {user_info['middle_name'].title()} {user_info['last_name'].title()}"
    
    # Passo 5: Exibimos o nome completo e o valor associado à chave 'location' do dicionário 'user_info'.
    print(f"{full_name} residente de {user_info['location']}.")

