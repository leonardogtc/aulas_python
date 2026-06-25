'''
CRIANDO LISTAS COM RANGE
Se quiser criar uma lista de números, você pode converter os resultados de
range() diretamente em uma lista usando a função list(). Quando
colocamos list() em torno de uma chamada à função range(), a saída será
uma lista de números.
'''
numeros = list(range(1, 6))
print(type(numeros))
print(numeros)

# --------------------
'''
Também podemos usar a função range() para dizer a Python que ignore
alguns números em um dado intervalo. Por exemplo, eis o modo de listar
os números pares entre 1 e 10:
'''
even_numbers = list(range(2, 11, 2))
print(even_numbers)

'''
Nesse exemplo, a função range() começa com o valor 2 e então soma 2 a
esse valor. O valor 2 é somado repetidamente até o valor final, que é 11, ser
alcançado ou ultrapassado, e o resultado a seguir é gerado:
'''
