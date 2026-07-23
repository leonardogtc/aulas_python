'''
Você pode armazenar seu prompt em uma variável e passá-la
para a função input(). Isso permite criar seu prompt com
várias linhas e escrever uma instrução input() clara.
'''
prompt = "Se você nos disser quem é, poderemos realizar um atendimento personalizado!\nQual o seu primeiro nome? "

nome = input(prompt)
print("Olá, " + nome + "!")