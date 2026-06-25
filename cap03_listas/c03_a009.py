"""
Removendo um item de acordo com o valor
---------------------------------------
Às vezes, você são saberá a posição do valor que quer remover de uma
lista. Se conhecer apenas o valor do item que deseja remover, o método
remove() poderá ser usado.
"""
motocicletas = ['honda', 'yamaha', 'suzuki', 'ducati', 'kawazaki']
print(motocicletas)

muito_cara = 'ducati'

print('----- REMOVENDO A DUCATI -----')
motocicletas.remove(muito_cara)
print(motocicletas)

print("\n----- MOTIVO -----")
print(
    f"Após consultas foi decidido que a {muito_cara.title()} "
    "fica acima do preço!")

'''
NOTA O método remove() apaga apenas a primeira ocorrência do valor que você
especificar. Se houver a possibilidade de o valor aparecer mais de uma vez na
lista, será necessário usar um laço para determinar se todas as ocorrências
desse valor foram removidas.
'''
