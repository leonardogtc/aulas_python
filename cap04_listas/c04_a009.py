# Tuplas (Tuples) em Python:
# 1. Imutáveis: Uma vez criadas, seus elementos não podem ser alterados, adicionados ou removidos.
# 2. Ordenadas: Os elementos mantêm uma ordem definida e constante, permitindo acesso por índice.
# 3. Permitem duplicatas: Podem conter múltiplos elementos com o mesmo valor.
# 4. Sintaxe: São representadas por parênteses `()` (embora a vírgula seja o real definidor de uma tupla).
# 5. Heterogêneas: Podem armazenar diferentes tipos de dados em uma única estrutura.
# OBS: Uma tupla se parece exatamente com uma lista, exceto por usar parênteses no lugar de colchetes.

# Exemplo prático de criação de uma tupla:
dias_da_semana = ('segunda', 'terça', 'quarta',
                  'quinta', 'sexta', 'sábado', 'domingo')

print(dias_da_semana)
print(f"O primeiro dia da semana é: {dias_da_semana[0]}")
print(f"O segundo dia da semana é: {dias_da_semana[1]}")
print(f"O terceiro dia da semana é: {dias_da_semana[2]}")
print(f"O quarto dia da semana é: {dias_da_semana[3]}")
print(f"O quinto dia da semana é: {dias_da_semana[4]}")
print(f"O sexto dia da semana é: {dias_da_semana[5]}")
print(f"O sétimo dia da semana é: {dias_da_semana[6]}")

# Exemplo prático de imutabilidade:
# dias_da_semana[0] = 'segundou'
# print(f"O primeiro dia da semana é: {dias_da_semana[0]}")

# Irá retornar: TypeError: 'tuple' object does not support item assignment

# Percorrendo os elementos de uma tupla com um laço
for dia in dias_da_semana:
    print(dia.title())

# Sobrescrevendo uma tupla (Tem que redeclarar a tupla)
dimensoes_retangulo = (4, 8)
print(dimensoes_retangulo)

dimensoes_retangulo = (12, 8)
print(dimensoes_retangulo)

