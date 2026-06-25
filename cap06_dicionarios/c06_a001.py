# Criação de um dicionário simples
# --------------------------------
# O dicionário simples a seguir armazena informações
# sobre um alienígena em particular
'''
1. Um dicionário em Python é uma coleção de pares chave-valor. Cada chave
é conectada a um valor, e você pode usar uma chave para acessar o valor
associado a ela.
2. O valor de uma chave pode ser um número, uma string,
uma lista ou até mesmo outro dicionário.
'''
alien_0 = {'color': 'verde', 'points': 5}
print(alien_0)

# Acessando a cor
print(alien_0['color'])
print(alien_0['points'])

print(
    f"A cor do alien é {alien_0['color']} e marcou {alien_0['points']} pontos."
)
