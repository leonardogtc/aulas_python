# Omitindo o bloco else
idade = 4

if idade < 4:
    preco = 0
elif idade < 18:
    preco = 5
elif idade < 65:
    preco = 10
elif idade >= 65:
    preco = 5

print(f"O preço da sua entrada é R$ {preco},00.")

'''
OBS: O bloco else é uma instrução que captura tudo. Ela corresponde a
qualquer condição não atendida por um teste if ou elif específicos e isso,
às vezes, pode incluir dados inválidos ou até mesmo maliciosos. Se você
tiver uma condição final específica para testar, considere usar um último
bloco elif e omitir o bloco else.
'''
