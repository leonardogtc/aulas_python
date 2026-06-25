'''
Usando break para sair de um laço
---------------------------------
Para sair de um laço while de imediato, sem executar qualquer código
restante no laço, independentemente do resultado de qualquer teste
condicional, utilize a instrução break. A instrução break direciona o fluxo
de seu programa; podemos usá-la para controlar quais linhas de código são
ou não são executadas, de modo que o programa execute apenas o código
que você quiser, quando você quiser.
'''
prompt = "\nPor favor, digite o nome da cidade que voc}ê visitou: "
prompt += "\nDigite 'sair' caso queira finalizar o programa! "

# Um laço que comece com while True executará indefinidamente, a
# menos que alcance uma instrução break.
while True:
    cidade = input(prompt)
    if cidade == 'sair':
        print('\nObrigado por usar nossos serviços!')
        break
    else:
        print("Eu adorei visitar " + cidade.title() + "!")

