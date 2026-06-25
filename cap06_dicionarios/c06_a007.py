# Percorrendo todas as chaves de um dicionário com um laço

linguagens_favoritas = {
    'oliver': 'python',
    'leonardo': 'java',
    'ezequiel': 'python',
    'lucia': 'php',
    'ayme': 'c',
}

if 'oliver' not in linguagens_favoritas.keys():
    for nome in linguagens_favoritas.keys():
        print(nome.title())

amigos = ['marcos', 'andre', 'ayme']

for name in linguagens_favoritas.keys():
    print(name.title())

    if name in amigos:
        print(f"Hello {name.title()}. Vi que sua linguagem favorita é {linguagens_favoritas[name].title()}.")

