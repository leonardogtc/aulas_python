# Percorrendo as chaves de um dicionário em ordem usando um laço
'''
Um dicionário sempre mantém uma conexão clara entre cada chave e seu
valor associado, mas você não obterá os itens de um dicionário em uma
ordem previsível. Isso não é um problema, pois, geralmente, queremos
apenas obter o valor correto associado a cada chave.
Uma maneira de fazer os itens serem devolvidos em determinada
sequência é ordenar as chaves à medida que são devolvidas no laço for.
'''

linguagens_favoritas = {
    'oliver': 'python',
    'leonardo': 'java',
    'ayme': 'rust',
    'lucia': 'c++',
    'ivonete': 'c ansi',
    'tatiana': 'java',
    'giovanna': 'c++',
    'murilo': 'c++',
    'fernanda': 'python',
}

# Lembrando que sorted não faz alteração na listagem original
for name in sorted(linguagens_favoritas.keys()):
    print(f"{name.title()}, obrigado por responder à pesquisa.")

print('--------------------------------------------')

# Percorrendo todos os valores de um dicionário com um laço
for valores in sorted(linguagens_favoritas.values()):
    print(f"{valores.title()} foi uma linguagem pesquisada.")

print('--------------------------------------------')
'''
Isso pode funcionar bem com uma quantidade pequena de
valores, mas em uma enquete com um número grande de entrevistados, o
resultado seria uma lista com muitas repetições. Para ver cada linguagem
escolhida sem repetições, podemos usar um conjunto (set).

O set elimina valores duplicados do conjunto.

Quando colocamos set() em torno de uma lista que contenha itens
duplicados, Python identifica os itens únicos na lista e cria um conjunto a
partir desses itens.
'''

for valores in set(linguagens_favoritas.values()):
    print(f"{valores.title()} foi uma linguagem pesquisada.")
