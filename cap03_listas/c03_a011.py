'''
reverse() --> Inverte a ordem da lista
O método reverse() muda a ordem de uma lista de forma permanente.
mas podemos restaurar a ordem original a qualquer momento aplicando
reverse() à mesma lista uma segunda vez.

sorted() --> Ordena a lista de forma permanente

'''
cidades = ['são paulo', 'rio de janeiro',
           'belo horizonte', 'curitiba', 'fortaleza']
print(cidades)
cidades.reverse()
print(cidades)

# Voltando a ordem anterior
cidades.reverse()
print(cidades)
