# Instruções IF
# Instruções if SIMPLES:

'''
Suponha que temos uma variável que representa a idade de uma pessoa e
queremos saber se essa pessoa tem idade suficiente para votar.
'''

idade = 19

if idade >= 18:
    print("Você tem idade suficiente para votar!")
    print("Você poderá votar assim que fizer 18 anos.")


# Instruções IF-ELSE:
'''
Suponha que queremos exibir uma mensagem diferente para usuários que
têm 18 anos ou mais e para aqueles que são mais jovens.
'''
age = 17

if idade >= 18:
    print("Você tem idade suficiente para votar!")
else:
    print("Desculpe, você ainda não tem idade para votar.")


# Instruções IF-ELIF-ELSE:
'''
Suponha que queremos exibir uma mensagem diferente para usuários que
têm 18 anos ou mais e para aqueles que são mais jovens.
'''
age = 24

if idade >= 18:
    print("Você tem idade suficiente para votar!")
    print("Você poderá votar assim que fizer 18 anos.")
elif idade < 18:
    print("Desculpe, você ainda não tem idade para votar.")
else:
    print("Você tem 21 anos.")

# if sem elif
age = 15

if idade >= 18:
    print("Você tem idade suficiente para votar!")
    print("Você poderá votar assim que fizer 18 anos.")
else:
    print("Desculpe, você ainda não tem idade para votar.")
