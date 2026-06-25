
linguagens_favoritas = {
    'oliver': 'python',
    'leonardo': 'java',
    'ezequiel': 'python',
    'lucia': 'php',
    'ayme':'c',
}

'''
----- BOAS PRÁTICAS -----
Incluir uma vírgula após o último par chave-valor também é uma boa prática;
assim você estará preparado para acrescentar um novo par chave-valor na
próxima linha.
'''

print(f"A linguagem favorita de Oliver é {linguagens_favoritas['oliver'].title()}.")

# Percorrendo dados
for nome, linguagem in linguagens_favoritas.items():
    print(f"A linguagem favorita de {nome.title()} é {linguagem.title()}!")
