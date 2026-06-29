# ----- Percorrendo um dicionário com um laço -----
user_0 = {
    'username': 'leonardogtc',
    'first': 'leonardo',
    'last': 'conceicao',
}


# As variáveis k e v representando Key (Chave) e Value (Valor)
# podem ser qualquer nome
for k, v in user_0.items():
    print("\nKey: " + k)
    print("Value:" + v)

print(user_0.items())
