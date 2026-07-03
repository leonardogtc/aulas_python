# Exercicio 1. Faça um programa que leia um número inteiro e imprima-o.
numero: int = int(input("Digite um número inteiro: "))
print("O número digitado foi:", numero)
print("\n")

# Exercicio 2. Faça um programa que peça para o usuário digitar três
# valores inteiro e imprima a soma deles.
num1: int = int(input("Digite o primeiro valor: "))
num2: int = int(input("Digite o segundo valor: "))
num3: int = int(input("Digite o terceiro valor: "))
soma: int = num1 + num2 + num3
print("A soma dos valores é:", soma)
print("\n")

# Exercício 3. Faça um programa que recebe três valores e apresente
# a soma dos quadrados dos valores lidos.
num1: int = int(input("Digite o primeiro valor: "))
num2: int = int(input("Digite o segundo valor: "))
num3: int = int(input("Digite o terceiro valor: "))
soma_quadrados: int = num1**2 + num2**2 + num3**2
print("A soma dos quadrados dos valores é:", soma_quadrados)
