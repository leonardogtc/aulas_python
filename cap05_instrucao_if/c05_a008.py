# Usando instruções if com listas

coberturas = ['pepperoni', 'cogumelos', 'mussarela extra', 'pimentões verdes']

for cobertura in coberturas:
    if cobertura == 'pimentões verdes':
        print("Desculpe! Estamos sem pimentões verdes no momento!")
    else:
        print(f"Adicionando {cobertura} à pizza.")

print("\nPizza concluída!")