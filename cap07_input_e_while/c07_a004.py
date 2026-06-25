'''
Usando int() para aceitar entradas numéricas
--------------------------------------------
* Se usarmos a função input(), Python interpretará tudo que o usuário
  fornecer como uma string. Dependendo da maneira como seja apresentado
  o resultado poderá causar um erro de tipo. Para resolver o problema
  pode-se utilizar a função int() para converter a representação em
  string de um número em uma representação numérica ou float() no caso
  do código abaixo.
'''

altura = input('Qual a sua altura? (usar: 0.00): ')
altura = float(altura)

if altura >= 1.80:
    print("Você é bem alto")
else:
    print("Sua altura está na média do provo brasileiro!")