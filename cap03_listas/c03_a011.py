# ==========================================
# Invertendo a Ordem de uma Lista com .reverse()
# Este código demonstra o uso do método reverse(),
# que inverte a ordem física dos elementos da lista.
# ==========================================

# NOTA DIDÁTICA IMPORTANTE:
# - reverse() NÃO ordena alfabeticamente ou numericamente. Ele apenas "espelha" a lista,
#   fazendo com que o primeiro item vire o último, o segundo vire o penúltimo, etc.
# - É permanente, mas você pode voltar ao estado original chamando .reverse() novamente.
# - A função sorted() (mencionada erroneamente em anotações anteriores) ordena
#   TEMPORARIAMENTE, não permanentemente.

# Lista inicial de cidades
cidades = ['são paulo', 'rio de janeiro',
           'belo horizonte', 'curitiba', 'fortaleza']
print(cidades)

# 1. Invertendo a ordem dos elementos permanentemente
# O último elemento ('fortaleza') vira o primeiro, e assim por diante.
cidades.reverse()
print(cidades)  # Exibirá: ['fortaleza', 'curitiba', 'belo horizonte', 'rio de janeiro', 'são paulo']

# 2. Restaurando a ordem original
# Chamando o reverse() uma segunda vez, a lista volta a ficar na ordem inicial.
cidades.reverse()
print(cidades)

