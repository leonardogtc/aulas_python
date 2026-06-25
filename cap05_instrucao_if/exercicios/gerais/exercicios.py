"""
Exercícios de Fixação: Testes Condicionais em Python (if-elif-else)

Complete o código de cada função de acordo com os requisitos descritos em sua docstring.
Você pode rodar os testes unitários em `test_exercicios.py` para verificar sua implementação.
"""

def exercicio_01_maioridade(idade: int) -> str:
    """
    Recebe a idade de uma pessoa e retorna:
    - "Maior de idade" se tiver 18 anos ou mais.
    - "Menor de idade" caso contrário.
    """
    # TODO: Implemente seu código aqui
    pass

def exercicio_02_par_ou_impar(numero: int) -> str:
    """
    Recebe um número inteiro e retorna:
    - "Par" se for divisível por 2 (resto da divisão igual a zero).
    - "Ímpar" caso contrário.
    """
    # TODO: Implemente seu código aqui
    pass

def exercicio_03_triangulos(a: float, b: float, c: float) -> str:
    """
    Recebe três lados (a, b, c) e retorna:
    - "Não é um triângulo" se os lados não cumprirem a condição de existência.
      (Condição: cada lado deve ser estritamente menor que a soma dos outros dois).
    - "Equilátero" se todos os três lados forem iguais.
    - "Isósceles" se apenas dois lados forem iguais.
    - "Escaleno" se todos os três lados forem diferentes.
    """
    # TODO: Implemente seu código aqui
    pass

def exercicio_04_calculadora(num1: float, num2: float, operacao: str) -> float | str:
    """
    Recebe dois números e uma operação representada por uma string: "+", "-", "*", "/".
    Retorna o resultado da operação.
    Se o operador não for um desses quatro, retorna "Operador Inválido".
    Se houver divisão por zero (num2 igual a zero e operacao "/"), retorna "Erro: Divisão por Zero".
    """
    # TODO: Implemente seu código aqui
    pass

def exercicio_05_ano_bissexto(ano: int) -> bool:
    """
    Recebe um ano e retorna True se ele for bissexto, e False caso contrário.
    Um ano é bissexto se:
    1. For divisível por 4 E não for divisível por 100, OU
    2. For divisível por 400.
    """
    # TODO: Implemente seu código aqui
    pass

def exercicio_06_imc(peso: float, altura: float) -> str:
    """
    Calcula o IMC = peso / (altura ** 2) e retorna a categoria correspondente:
    - IMC < 18.5: "Abaixo do peso"
    - 18.5 <= IMC < 25.0: "Peso normal"
    - 25.0 <= IMC < 30.0: "Sobrepeso"
    - IMC >= 30.0: "Obesidade"
    """
    # TODO: Implemente seu código aqui
    pass

def exercicio_07_aprovacao_escolar(nota1: float, nota2: float, nota3: float) -> str:
    """
    Calcula a média aritmética simples das 3 notas e classifica o aluno:
    - Média >= 7.0: "Aprovado"
    - 5.0 <= Média < 7.0: "Recuperação"
    - Média < 5.0: "Reprovado"
    """
    # TODO: Implemente seu código aqui
    pass

def exercicio_08_desconto_compra(valor_compra: float) -> tuple[float, float]:
    """
    Recebe o valor total de uma compra e aplica descontos progressivos:
    - Compra acima de R$ 500.00: 15% de desconto.
    - Compra de R$ 200.00 até R$ 500.00 (inclusive): 10% de desconto.
    - Compra menor que R$ 200.00: Sem desconto.
    
    Retorna uma tupla contendo (valor_desconto, valor_final), ambas arredondadas para 2 casas decimais.
    """
    # TODO: Implemente seu código aqui
    pass

def exercicio_09_aprovacao_emprestimo(salario: float, valor_casa: float, anos_pagar: int) -> str:
    """
    Calcula o valor da prestação mensal da casa (valor_casa dividido pelo total de meses a pagar).
    O empréstimo é concedido se o valor da prestação não ultrapassar 30% do salário mensal.
    Retorna "Aprovado" se concedido, ou "Negado" caso contrário.
    """
    # TODO: Implemente seu código aqui
    pass

def exercicio_10_classificacao_clima(temperatura: float) -> str:
    """
    Classifica a temperatura em graus Celsius de acordo com as faixas:
    - Menor que 15.0°C: "Frio"
    - De 15.0°C até 25.0°C (inclusive): "Agradável"
    - De 26.0°C até 35.0°C (inclusive): "Quente"
    - Maior que 35.0°C: "Muito Quente"
    """
    # TODO: Implemente seu código aqui
    pass
