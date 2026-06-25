'''
Deixando o usuário decidir quando quer sair
-------------------------------------------
'''

prompt = "Me diga algo para que eu repita para você: "
prompt += "\nDigite <<< sair >>> para finalizar o programa. "

'''
Se Python não tiver nada para comparar, ele não será capaz de continuar
executando o programa. Para resolver esse problema, garantimos que message
receba um valor inicial. Embora seja apenas uma string vazia, ela fará
sentido para Python e permitirá que a comparação que faz o laço while
funcionar seja feita.
'''
mensagem = ""

while mensagem != 'sair':
    mensagem = input(prompt)
    if mensagem != 'sair':
        print(mensagem)
