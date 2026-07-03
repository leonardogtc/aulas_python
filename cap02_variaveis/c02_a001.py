# Recebendo dados do usuário
# --------------------------
# Exibe uma mensagem no terminal perguntando o nome do usuário
print("Olá! Qual o seu nome?")
# Lê a entrada que o usuário digitar no terminal e a guarda na variável 'nome'
nome = input()

# Exibe uma mensagem no terminal perguntando a idade do usuário
print('Qual a sua idade?')
# Lê a entrada que o usuário digitar no terminal e a guarda na variável 'idade'
idade = input()

# Exibe uma mensagem de boas-vindas formatada na tela, substituindo os operadores "%s" pelos valores das variáveis (nome, idade)
print('Seja bem vindo %s, você tem %s anos' % (nome, idade))

# ou
print('Seja bem vindo {0}, você tem {1} anos'.format(nome, idade))

# ou (Prefiro dessa maneira)
print(f'Seja bem vindo {nome}, você tem {idade} anos')