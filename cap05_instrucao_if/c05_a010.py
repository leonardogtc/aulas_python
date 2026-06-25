# Usando várias listas

coberturas_disponiveis = ['mussarela extra', 'pepperoni',
                          'cogumelos', 'bacon', 'cebola', 'pimentão verde', 'azeitonas']
coberturas_solicitadas = ['pepperoni', 'cogumelos',
                          'mussarela extra', 'pimentão verde', 'molho de pimenta']

for cobertura in coberturas_solicitadas:
    if cobertura in coberturas_disponiveis:
        print(f"Adicionando {cobertura} à pizza.")
    else:
        print(f"Desculpe! Não temos {cobertura} disponível.")

print("\nPizza concluída!")
