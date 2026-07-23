# Operador Módulo (retorna o resto da divisão entre dois números)
prompt = "Entre um número inteiro e te direi se é par ou impar!\nDigite o número desejado: "

numero = int(input(prompt))

if numero % 2 == 0:
    print(f"O número {numero} é par!")
else:
    print(f"O número {numero} é impar!")