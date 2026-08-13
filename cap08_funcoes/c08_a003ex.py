"""
EXERCÍCIOS 8.1 e 8.2

8.1 – Mensagem: Escreva uma função chamada display_message() que mostre
uma frase informando a todos o que você está aprendendo neste capítulo. Chame
a função e certifique-se de que a mensagem seja exibida corretamente.

8.2 – Livro favorito: Escreva uma função chamada favorite_book() que aceite
um parâmetro title. A função deve exibir uma mensagem como 'Um dos meus
livros favoritos é Alice no país das maravilhas'. Chame a função e não
se esqueça de incluir o título do livro como argumento na chamada da função.
"""

# --- EXERCÍCIO 8.1 ---
# Definição da função 'display_message' sem parâmetros
def display_message():
    """Exibe uma mensagem sobre o aprendizado do capítulo atual."""
    print("Neste capítulo, estou aprendendo sobre funções em Python!")

# Chamada da função para testar o envio de mensagem
display_message()


# --- EXERCÍCIO 8.2 ---
# Definição da função 'favorite_book' que recebe o parâmetro 'title'
def favorite_book(title):
    """Exibe uma mensagem informando qual é o livro favorito fornecido."""
    # Usamos f-string para interpolar a variável 'title' na mensagem
    print(f"Um dos meus livros favoritos é {title}.")

# Chamada da função passando o título do livro como argumento
favorite_book("Alice no País das Maravilhas")
