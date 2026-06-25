# Usando um laço while com listas e dicionários
# ---------------------------------------------

'''
Contudo, para controlar muitos usuários e informações, precisaremos
usar listas e dicionários com nossos laços while.
Um laço for é eficiente para percorrer uma lista, mas você não deve
modificar uma lista em um laço for, pois Python terá problemas para
manter o controle dos itens da lista. Para modificar uma lista enquanto
trabalhar com ela, utilize um laço while. Usar laços while com listas e
dicionários permite coletar, armazenar e organizar muitas entradas a
fim de analisá-las e apresentá-las posteriormente.
'''

# Transferindo itens de uma lista para outra
# ------------------------------------------

# Passo 1: Começamos com uma lista de usuários não confirmados
# e uma lista vazia que receberá os usuários confirmados.
usuarios_nao_confirmados = ['alice', 'coelho', 'chapeleiro']
usuarios_confirmados = []

# Passo 2: O laço 'while' executa enquanto houver itens em 'usuarios_nao_confirmados'.
# Em Python, listas com elementos são avaliadas como True, e listas vazias como False.
while usuarios_nao_confirmados:
    # Passo 3: O método '.pop()' remove e retorna o último elemento da lista.
    # Com isso, a lista vai diminuindo a cada rodada do laço.
    usuarios_atual = usuarios_nao_confirmados.pop()

    # Passo 4: Exibimos a verificação do usuário atual formatado com a primeira letra maiúscula (.title()).
    print(f"Verificado usuário: {usuarios_atual.title()}")

    # Passo 5 (Correção): Adicionamos o usuário verificado à lista de confirmados.
    # Sem esta linha, a lista 'usuarios_confirmados' permaneceria vazia.
    usuarios_confirmados.append(usuarios_atual)

# Passo 6: Após processar todos os usuários, exibimos o cabeçalho final.
print("\nOs usuários a seguir foram confirmados:")

# Passo 7: Usamos um laço 'for' para percorrer e exibir todos os usuários agora confirmados.
for usuario_confirmado in usuarios_confirmados:
    print(usuario_confirmado.title())

