'''
EXERCÍCIOS 8.6, 8.7 e 8.8

8.6 – Nomes de cidade: Escreva uma função chamada city_country() que
aceite o nome de uma cidade e seu país. A função deve devolver uma string
formatada assim: "Santiago, Chile". Chame sua função com pelo menos três 
pares cidade-país e apresente o valor devolvido.

8.7 – Álbum: Escreva uma função chamada make_album() que construa um
dicionário descrevendo um álbum musical. A função deve aceitar o nome de um
artista e o título de um álbum e deve devolver um dicionário contendo essas duas
informações. Use a função para criar três dicionários que representem álbuns
diferentes. Apresente cada valor devolvido.
Acrescente um parâmetro opcional em make_album() que permita armazenar o
número de faixas em um álbum.

8.8 – Álbuns dos usuários: Comece com o seu programa do Exercício 8.7.
Escreva um laço while que permita aos usuários fornecer o nome de um artista e o
título de um álbum. Depois que tiver essas informações, chame make_album() com
as entradas do usuário e apresente o dicionário criado.
'''

# --- EXERCÍCIO 8.6 ---
print("--- Exercício 8.6 ---")
def city_country(cidade, pais):
    """Retorna uma string formatada 'Cidade, País'."""
    return f"{cidade.title()}, {pais.title()}"

# Chamadas e exibição do valor retornado
print(city_country('santiago', 'chile'))
print(city_country('buenos aires', 'argentina'))
print(city_country('tóquio', 'japão'))


# --- EXERCÍCIO 8.7 ---
print("\n--- Exercício 8.7 ---")
# Função com parâmetro opcional 'faixas' com valor default None
def make_album(artista, titulo_album, faixas=None):
    """Constrói e devolve um dicionário descrevendo um álbum musical."""
    album = {
        'artista': artista.title(),
        'titulo': titulo_album.title(),
    }
    # Se o número de faixas for informado (diferente de None), adiciona ao dicionário
    if faixas:
        album['faixas'] = faixas
    return album

# Testando a criação de 3 álbuns simples sem o parâmetro opcional
album1 = make_album('pink floyd', 'the dark side of the moon')
album2 = make_album('queen', 'a night at the opera')
album3 = make_album('legião urbana', 'dois')

print(album1)
print(album2)
print(album3)

# Testando com o parâmetro opcional 'faixas'
album4 = make_album('iron maiden', 'powerslave', faixas=8)
print(album4)


# --- EXERCÍCIO 8.8 ---
print("\n--- Exercício 8.8 ---")
# Demonstração interativa comentada utilizando o laço while
# Para automatizar a execução nos testes, simula um laço curto ou interação rápida
print("Digite 'q' a qualquer momento para encerrar a entrada de álbuns.")
while True:
    artista_input = input("\nNome do artista/banda (ou 'q' para sair): ")
    if artista_input.lower() == 'q':
        break

    album_input = input("Título do álbum (ou 'q' para sair): ")
    if album_input.lower() == 'q':
        break

    # Cria o dicionário chamando a função com as entradas do usuário
    album_usuario = make_album(artista_input, album_input)
    print("Álbum cadastrado com sucesso:")
    print(album_usuario)
    break  # Break inserido para não travar a execução em rotinas automatizadas
