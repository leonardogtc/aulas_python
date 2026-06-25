"""
Gabarito com as resoluções dos exercícios de testes condicionais.
Use para fins de consulta ou comparação de soluções.
"""

def exercicio_01_maioridade(idade: int) -> str:
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

def exercicio_02_par_ou_impar(numero: int) -> str:
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

def exercicio_03_triangulos(a: float, b: float, c: float) -> str:
    # Condição de existência de um triângulo: cada lado deve ser menor que a soma dos outros dois
    if (a >= b + c) or (b >= a + c) or (c >= a + b):
        return "Não é um triângulo"
    
    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or a == c:
        return "Isósceles"
    else:
        return "Escaleno"

def exercicio_04_calculadora(num1: float, num2: float, operacao: str) -> float | str:
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        if num2 == 0:
            return "Erro: Divisão por Zero"
        return num1 / num2
    else:
        return "Operador Inválido"

def exercicio_05_ano_bissexto(ano: int) -> bool:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

def exercicio_06_imc(peso: float, altura: float) -> str:
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25.0:
        return "Peso normal"
    elif imc < 30.0:
        return "Sobrepeso"
    else:
        return "Obesidade"

def exercicio_07_aprovacao_escolar(nota1: float, nota2: float, nota3: float) -> str:
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperação"
    else:
        return "Reprovado"

def exercicio_08_desconto_compra(valor_compra: float) -> tuple[float, float]:
    if valor_compra > 500.0:
        desconto = valor_compra * 0.15
    elif valor_compra >= 200.0:
        desconto = valor_compra * 0.10
    else:
        desconto = 0.0
    
    valor_final = valor_compra - desconto
    return round(desconto, 2), round(valor_final, 2)

def exercicio_09_aprovacao_emprestimo(salario: float, valor_casa: float, anos_pagar: int) -> str:
    meses = anos_pagar * 12
    prestacao = valor_casa / meses
    limite = salario * 0.30
    
    if prestacao <= limite:
        return "Aprovado"
    else:
        return "Negado"

def exercicio_10_classificacao_clima(temperatura: float) -> str:
    if temperatura < 15.0:
        return "Frio"
    elif temperatura <= 25.0:
        return "Agradável"
    elif temperatura <= 35.0:
        return "Quente"
    else:
        return "Muito Quente"
