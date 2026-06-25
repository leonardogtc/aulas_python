carros = ['audi', 'bmw', 'subaru', 'toyota']

# Exemplo simples (percorrendo lista e decidindo)
for carro in carros:
    if carro == 'bmw':
        print(carro.upper())
    else:
        print(carro.title())


# Igualdade ( == )
meu_carro = "BMW"
if meu_carro == "bmw":
    print(f"Meu carro é um {meu_carro}")

# Resolvendo o problema do case sensitive
if meu_carro.lower() == "bmw":
    print(f"Meu carro é um {meu_carro}")

# Não igual (diferente)
# ( != )
sorvete_preferido = 'Côco'
sorvete = 'Tangerina'

if sorvete.lower() != sorvete_preferido.lower():
    print("Não quero, obrigado!")