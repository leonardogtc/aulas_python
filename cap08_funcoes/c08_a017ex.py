'''
EXERCÍCIOS 8.9, 8.10 e 8.11

8.9 – Mágicos: Crie uma lista de nomes de mágicos. Passe a lista para uma
função chamada show_magicians() que exiba o nome de cada mágico da lista.

8.10 – Grandes mágicos: Comece com uma cópia de seu programa do Exercício
8.9. Escreva uma função chamada make_great() que modifique a lista de
mágicos acrescentando a expressão 'o Grande' ao nome de cada mágico. Chame
show_magicians() para ver se a lista foi realmente modificada.

8.11 – Mágicos inalterados: Comece com o trabalho feito no Exercício 8.10.
Chame a função make_great() com uma cópia da lista de nomes de mágicos.
Devolva a nova lista e armazene-a em uma lista separada.
'''

# --- EXERCÍCIO 8.9 ---
print("--- Exercício 8.9 ---")
# Função para exibir cada mágico da lista
def show_magicians(magicos):
    """Exibe o nome de cada mágico da lista."""
    for magico in magicos:
        print(magico)

# Lista inicial de mágicos
magicians = ['Houdini', 'David Copperfield', 'Penn & Teller']
show_magicians(magicians)


# --- EXERCÍCIO 8.10 ---
print("\n--- Exercício 8.10 ---")
# Função que MODIFICA a lista in-place (no próprio local da memória)
def make_great(magicos):
    """Modifica a lista de mágicos adicionando 'o Grande' a cada nome."""
    # Usamos range(len(magicos)) para iterar pelos índices e alterar o valor de cada posição diretamente
    for i in range(len(magicos)):
        magicos[i] = f"{magicos[i]} o Grande"

# Copiamos a lista para demonstrar o 8.10 sem estragar os testes seguintes
magicos_exercicio_810 = magicians[:]
make_great(magicos_exercicio_810)
show_magicians(magicos_exercicio_810)


# --- EXERCÍCIO 8.11 ---
print("\n--- Exercício 8.11 ---")
# Função que cria e RETORNA uma nova lista com 'o Grande', sem modificar a lista recebida
def make_great_copia(magicos):
    """Retorna uma nova lista com 'o Grande' adicionado a cada nome de mágico."""
    grandes_magicos = []
    for magico in magicos:
        grandes_magicos.append(f"{magico} o Grande")
    return grandes_magicos

# Enviamos uma cópia magicians[:] para a função e capturamos a nova lista retornada
novos_magicos = make_great_copia(magicians[:])

print("Lista Original (inalterada):")
show_magicians(magicians)

print("\nNova Lista (com 'o Grande'):")
show_magicians(novos_magicos)
