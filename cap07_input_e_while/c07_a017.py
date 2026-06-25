'''
Preenchendo um dicionário com dados de entrada do usuário
---------------------------------------------------------

Podemos pedir a quantidade de entrada que for necessária a cada passagem
por um laço while. Vamos criar um programa de enquete em que cada
passagem pelo laço solicita o nome do participante e uma resposta.
Armazenaremos os dados coletados em um dicionário.
'''

respostas = {}

# Define uma flag para indicar que a enquete está ativa
sondagem_ativa = True

while sondagem_ativa:
    # Pede o nome da pessoa e a resposta
    nome = input("\nQual o seu nome? ")
    resposta = input("Que montanha você gostaria de escalar algum dia? ")

    # Armazena a resposta no dicionário
    respostas[nome] = resposta

    # Descobre se outra pessoa vai responder à enquete
    repete = input('Gostaria de deixar outra pessoa responder? (S/N) ')
    if repete == 'N' or repete == 'n':
        sondagem_ativa = False

# A enquete foi concluída. Mostra os resultados
print("\n----- RESULTADOS DA ENQUETE -----")
for nome, resposta in respostas.items():
    print(nome + " você gostaria de escalar " + resposta + ".")
