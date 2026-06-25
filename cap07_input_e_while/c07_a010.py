'''
USANDO UMA FLAG
---------------
Para um programa que deva executar somente enquanto muitas
condições forem verdadeiras, podemos definir uma variável que determina
se o programa como um todo deve estar ativo. Essa variável, chamada de
flag, atua como um sinal para o programa.
'''

prompt = "Me diga algo para que eu repita para você: "
prompt += "\nDigite <<< sair >>> para finalizar o programa. "


ativo = True
while ativo:
    mensagem = input(prompt)

    if mensagem == 'sair':
        ativo = False
    else:
        print(mensagem)
