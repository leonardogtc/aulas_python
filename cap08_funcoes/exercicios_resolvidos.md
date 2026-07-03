# Resoluções dos Exercícios: Capítulo 8 - Funções

Este arquivo apresenta soluções completas e comentadas para os 50 exercícios propostos no caderno de prática. Todas as soluções seguem as convenções de estilo do Python (PEP 8) e focam na clareza do aprendizado.

---

## Parte 1: Conceitos Básicos, Definição e Docstrings

### Exercício 1: Mensagem Simples
```python
def mostrar_mensagem():
    print("Neste capítulo, estou aprendendo a organizar meu código em funções reutilizáveis!")

# Chamada da função
mostrar_mensagem()
```

### Exercício 2: Saudação Personalizada
```python
def saudar_usuario(nome):
    print(f"Olá, {nome}! Seja bem-vindo ao estudo de funções!")

# Chamadas com diferentes argumentos
saudar_usuario("Leonardo")
saudar_usuario("Maria")
```

### Exercício 3: Documentando uma Função
```python
def somar_dois_numeros(a, b):
    """Recebe dois números (a e b) e imprime a soma deles na tela."""
    soma = a + b
    print(f"A soma de {a} e {b} é: {soma}")

# Chamando a função
somar_dois_numeros(5, 7)

# Acessando a docstring
print("\nExibindo docstring:")
print(somar_dois_numeros.__doc__)
```

### Exercício 4: Área do Quadrado
```python
def calcular_area_quadrado(lado):
    area = lado ** 2
    print(f"A área do quadrado com lado {lado} é {area}.")

# Teste da função
calcular_area_quadrado(4)
```

### Exercício 5: Conversor de Temperatura
```python
def celsius_para_fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    print(f"{celsius}°C equivale a {fahrenheit}°F.")

# Teste da função
celsius_para_fahrenheit(25)
```

### Exercício 6: Contador de Caracteres
```python
def contar_caracteres(texto):
    total = len(texto)
    print(f"O texto fornecido possui {total} caracteres (incluindo espaços).")

# Teste da função
contar_caracteres("Estudando funções em Python.")
```

### Exercício 7: Verificação de Paridade
```python
def verificar_paridade(numero):
    if numero % 2 == 0:
        print(f"O número {numero} é Par.")
    else:
        print(f"O número {numero} é Ímpar.")

# Testes da função
verificar_paridade(10)
verificar_paridade(7)
verificar_paridade(0)
```

### Exercício 8: Ajuda Interativa com Docstrings
```python
def multiplicar_valores(x, y):
    """
    Multiplica dois valores numéricos x e y.
    
    Parâmetros:
    x (int/float): O primeiro operando.
    y (int/float): O segundo operando.
    
    Retorna:
    Exibe a multiplicação dos valores diretamente no console.
    """
    print(f"O resultado de {x} * {y} é {x * y}")

# Exibe a ajuda nativa
help(multiplicar_valores)
```

---

## Parte 2: Parâmetros e Argumentos (Posicionais, Nomeados e Default)

### Exercício 9: Pet Shop
```python
def descrever_pet(tipo, nome):
    print(f"\nEu tenho um {tipo}.")
    print(f"Meu {tipo} se chama {nome.title()}.")

# Chamada usando argumentos posicionais
descrever_pet('cachorro', 'toby')
```

### Exercício 10: Argumentos Nomeados
```python
def descrever_pet(tipo, nome):
    print(f"\nEu tenho um {tipo}.")
    print(f"Meu {tipo} se chama {nome.title()}.")

# Chamadas com argumentos nomeados em ordem invertida
descrever_pet(nome='harry', tipo='hamster')
descrever_pet(tipo='gato', nome='mingau')
```

### Exercício 11: Marca Padrão
```python
def descrever_carro(modelo, marca='Chevrolet'):
    print(f"Carro: {modelo} | Fabricante: {marca}")

# Utiliza a marca default 'Chevrolet'
descrever_carro('Onix')

# Sobrescreve a marca default para 'Ford'
descrever_carro('Mustang', 'Ford')
```

### Exercício 12: Confecção de Camiseta
```python
def fazer_camiseta(tamanho, estampa):
    print(f"Confecção: Camiseta tamanho '{tamanho}' com a estampa '{estampa}'.")

# 1. Argumentos posicionais
fazer_camiseta('M', 'Python Dev')

# 2. Argumentos nomeados
fazer_camiseta(estampa='Geek Power', tamanho='G')
```

### Exercício 13: Camisetas Grandes por Padrão
```python
def fazer_camiseta(tamanho='G', estampa='Eu amo Python'):
    print(f"Confecção: Camiseta tamanho '{tamanho}' com a estampa '{estampa}'.")

# 1. Camiseta G com a mensagem padrão
fazer_camiseta()

# 2. Camiseta M com a mensagem padrão
fazer_camiseta(tamanho='M')

# 3. Camiseta PP com uma estampa personalizada
fazer_camiseta(tamanho='PP', estampa='Hello World')
```

### Exercício 14: Descrição de Cidades
```python
def descrever_cidade(cidade, pais='Brasil'):
    print(f"{cidade.title()} fica no(a) {pais.title()}.")

# Chamadas variadas
descrever_cidade('São Paulo')
descrever_cidade('Rio de Janeiro')
descrever_cidade('Paris', 'França')
```

### Exercício 15: Cálculo de Preço com Desconto Opcional
```python
def calcular_preco(nome_produto, preco_original, desconto=0.0):
    preco_final = preco_original - (preco_original * desconto)
    print(f"Produto: {nome_produto}, Preço Final: R${preco_final:.2f}.")

# Sem aplicar desconto
calcular_preco('Livro', 50.0)

# Aplicando desconto de 15% (0.15)
calcular_preco('Notebook', 3000.0, 0.15)
```

### Exercício 16: O Impacto da Ordem dos Posicionais
```python
def apresentar_idade(nome, idade):
    print(f"{nome} tem {idade} anos de idade.")

# Se invertermos por engano na passagem dos posicionais:
apresentar_idade(25, 'Leonardo')

# O Python não gera erro de sintaxe ou execução (já que 'nome' recebe 25 e 'idade' recebe 'Leonardo'),
# mas a saída fica semanticamente incorreta: "25 tem Leonardo anos de idade."
```

### Exercício 17: Ficha de Endereço Completa
```python
def exibir_endereco(rua, cidade, estado, cep, numero='S/N'):
    print(f"Endereço: Rua {rua}, Nº {numero} - CEP: {cep} - {cidade}/{estado}")

# Chamadas com diferentes combinações de argumentos
exibir_endereco("Paulista", "São Paulo", "SP", "01311-000", numero="1000")
exibir_endereco("das Flores", "Curitiba", "PR", "80000-000")
```

---

## Parte 3: Retorno de Valores

### Exercício 18: Formatando Nome Completo
```python
def obter_nome_formatado(nome, sobrenome):
    completo = f"{nome} {sobrenome}"
    return completo.title()

# Capturando e exibindo o valor retornado
nome_usuario = obter_nome_formatado('leonardo', 'silva')
print(f"Nome completo formatado: {nome_usuario}")
```

### Exercício 19: Nome do Meio Opcional
```python
def obter_nome_formatado(nome, sobrenome, nome_do_meio=''):
    if nome_do_meio:
        completo = f"{nome} {nome_do_meio} {sobrenome}"
    else:
        completo = f"{nome} {sobrenome}"
    return completo.title()

# Chamada sem o nome do meio
print(obter_nome_formatado('joão', 'silva'))

# Chamada com o nome do meio
print(obter_nome_formatado('maria', 'souza', 'aparecida'))
```

### Exercício 20: Dicionário de Cadastro de Usuário
```python
def construir_usuario(nome, email, telefone):
    usuario = {
        'nome': nome,
        'email': email,
        'telefone': telefone,
    }
    return usuario

perfil = construir_usuario('Ana', 'ana@email.com', '1199999-9999')
print(perfil)
```

### Exercício 21: Cadastro com Campo Opcional
```python
def construir_usuario(nome, email, telefone, idade=None):
    usuario = {
        'nome': nome,
        'email': email,
        'telefone': telefone,
    }
    if idade is not None:
        usuario['idade'] = idade
    return usuario

# Teste sem idade
print(construir_usuario('Carlos', 'carlos@email.com', '118888-8888'))

# Teste com idade
print(construir_usuario('Carlos', 'carlos@email.com', '118888-8888', idade=30))
```

### Exercício 22: Operações Matemáticas Básicas
```python
def calcular_operacoes(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b if b != 0 else float('nan')
    return soma, subtracao, multiplicacao, divisao

# Desempacotando os retornos
s, sub, m, d = calcular_operacoes(10, 2)
print(f"Soma: {s}, Subtração: {sub}, Multiplicação: {m}, Divisão: {d}")
```

### Exercício 23: Retornando o Maior de Três Números
```python
def encontrar_maior(n1, n2, n3):
    return max(n1, n2, n3)

maior = encontrar_maior(15, 42, 27)
print(f"O maior número é: {maior}")
```

### Exercício 24: Cidade e País Formatados
```python
def cidade_pais(cidade, pais):
    return f"{cidade.title()}, {pais.title()}"

print(cidade_pais('santiago', 'chile'))
print(cidade_pais('tóquio', 'japão'))
print(cidade_pais('nova iorque', 'estados unidos'))
```

### Exercício 25: Cadastro de Álbuns Musicais
```python
def make_album(artista, titulo, faixas=None):
    album = {
        'artista': artista.title(),
        'titulo': titulo.title(),
    }
    if faixas:
        album['faixas'] = faixas
    return album

# Criando álbuns diferentes
print(make_album('Pink Floyd', 'The Dark Side of the Moon'))
print(make_album('Daft Punk', 'Discovery', faixas=14))
print(make_album('Queen', 'A Night at the Opera'))
```

### Exercício 26: Cadastro com Loop While
```python
def make_album(artista, titulo, faixas=None):
    album = {
        'artista': artista.title(),
        'titulo': titulo.title(),
    }
    if faixas:
        album['faixas'] = faixas
    return album

# Laço interativo
while True:
    print("\n--- Cadastro de Álbum (digite 'q' para sair) ---")
    artista = input("Artista: ")
    if artista.lower() == 'q':
        break
    titulo = input("Título do Álbum: ")
    if titulo.lower() == 'q':
        break
    
    album_cadastrado = make_album(artista, titulo)
    print("\nÁlbum cadastrado:")
    print(album_cadastrado)
```

---

## Parte 4: Passando e Modificando Listas em Funções

### Exercício 27: Mensagens em Massa
```python
def exibir_mensagens(lista_mensagens):
    for msg in lista_mensagens:
        print(f"Mensagem: {msg}")

mensagens = [
    "Aprender Python é divertido!",
    "Funções nos ajudam a evitar repetição.",
    "Módulos organizam o código."
]
exibir_mensagens(mensagens)
```

### Exercício 28: Enviando Mensagens
```python
def enviar_mensagens(lista_pendentes, lista_enviadas):
    while lista_pendentes:
        # Extrai a primeira mensagem da fila (FIFO)
        mensagem = lista_pendentes.pop(0)
        print(f"Enviando mensagem: '{mensagem}'...")
        lista_enviadas.append(mensagem)

pendentes = ["Mensagem 1", "Mensagem 2", "Mensagem 3"]
enviadas = []

enviar_mensagens(pendentes, enviadas)
print(f"\nLista de Pendentes final: {pendentes}")
print(f"Lista de Enviadas final: {enviadas}")
```

### Exercício 29: Preservando a Lista Original
```python
# Continuando do Exercício 28, mas criando novas listas:
pendentes = ["Mensagem A", "Mensagem B", "Mensagem C"]
enviadas = []

# Passamos a lista de pendentes fatiada [:] para enviar uma cópia
enviar_mensagens(pendentes[:], enviadas)

print("\n--- Após execução com cópia [:] ---")
print(f"Pendentes originais (preservados): {pendentes}")
print(f"Enviadas: {enviadas}")
```

### Exercício 30: Dobrar Valores de uma Lista
```python
def dobrar_valores(numeros):
    for i in range(len(numeros)):
        numeros[i] *= 2

valores = [1, 2, 3, 4, 5]
dobrar_valores(valores)
print(f"Valores dobrados (in-place): {valores}") # Lista original foi alterada
```

### Exercício 31: Filtrar Números Pares
```python
def filtrar_pares(numeros):
    pares = [num for num in numeros if num % 2 == 0]
    return pares

originais = [1, 2, 3, 4, 5, 6]
apenas_pares = filtrar_pares(originais)
print(f"Pares retornados: {apenas_pares}")
print(f"Originais (inalterados): {originais}")
```

### Exercício 32: Atualização de Status
```python
def atualizar_status_pedidos(pedidos):
    for pedido in pedidos:
        pedido['status'] = 'Concluído'

lista_pedidos = [
    {'id': 101, 'status': 'Pendente'},
    {'id': 102, 'status': 'Em processamento'},
]
atualizar_status_pedidos(lista_pedidos)
print(lista_pedidos) # Os dicionários foram modificados
```

### Exercício 33: Mágicos e Grandes Mágicos
```python
def show_magicians(magicos):
    for magico in magicos:
        print(magico)

def make_great(magicos):
    for i in range(len(magicos)):
        magicos[i] = f"{magicos[i]} o Grande"

magicos_lista = ["Houdini", "David Copperfield", "Penn & Teller"]
make_great(magicos_lista)
show_magicians(magicos_lista)
```

### Exercício 34: Evitando Grandes Mágicos Inalterados
```python
def show_magicians(magicos):
    for magico in magicos:
        print(magico)

def make_great_copia(magicos):
    nova_lista = []
    for magico in magicos:
        nova_lista.append(f"{magico} o Grande")
    return nova_lista

magicos_originais = ["Houdini", "Copperfield"]
# Passando uma cópia e armazenando o retorno
magicos_grandes = make_great_copia(magicos_originais[:])

print("Originais:")
show_magicians(magicos_originais)
print("\nModificados:")
show_magicians(magicos_grandes)
```

### Exercício 35: Analisador de Listas
```python
def analisar_notas(notas):
    maior = max(notas)
    menor = min(notas)
    media = sum(notas) / len(notas) if notas else 0
    aprovado = media >= 7.0
    return {
        'maior_nota': maior,
        'menor_nota': menor,
        'media': media,
        'aprovado': aprovado
    }

resultado = analisar_notas([8.5, 9.0, 6.0, 7.5])
print(resultado)
```

---

## Parte 5: Argumentos Arbitrários (`*args` e `**kwargs`)

### Exercício 36: Pedido de Sanduíche (`*args`)
```python
def montar_sanduiche(*itens):
    print("\nPreparando um sanduíche com os seguintes ingredientes:")
    for item in itens:
        print(f"- {item}")

montar_sanduiche("presunto", "queijo", "alface", "tomate")
```

### Exercício 37: Várias Chamadas de Sanduíches
```python
# A mesma função suporta qualquer quantidade de argumentos posicionais:
montar_sanduiche("pasta de amendoim")
montar_sanduiche("frango desfiado", "requeijão")
montar_sanduiche()
```

### Exercício 38: Misturando Tamanho e Ingredientes
```python
def montar_sanduiche_tamanho(tamanho, *itens):
    print(f"\nPreparando um sanduíche {tamanho} com os seguintes ingredientes:")
    for item in itens:
        print(f"- {item}")

# O parâmetro regular 'tamanho' deve vir ANTES de '*itens'
montar_sanduiche_tamanho("Grande", "carne", "queijo duplo", "bacon")
```

### Exercício 39: Somador Infinito
```python
def somar_todos(*numeros):
    return sum(numeros)

print(somar_todos())
print(somar_todos(10))
print(somar_todos(10, 20, 30))
```

### Exercício 40: Perfil de Usuário (`**kwargs`)
```python
def construir_perfil(nome, sobrenome, **informacoes):
    perfil = {
        'nome': nome,
        'sobrenome': sobrenome,
    }
    for chave, valor in informacoes.items():
        perfil[chave] = valor
    return perfil

usuario_perfil = construir_perfil('Leonardo', 'Silva', profissao='Programador', cidade='São Paulo')
print(usuario_perfil)
```

### Exercício 41: Cadastro de Carros (`**kwargs`)
```python
def armazenar_carro(fabricante, modelo, **detalhes):
    carro = {
        'fabricante': fabricante,
        'modelo': modelo,
    }
    for chave, valor in detalhes.items():
        carro[chave] = valor
    return carro

meu_carro = armazenar_carro('Toyota', 'Corolla', cor='prata', ano=2022, motor='2.0')
print(meu_carro)
```

### Exercício 42: Concatenação Inteligente de Strings
```python
def formatar_mensagem(*palavras, separador=' '):
    return separador.join(palavras)

print(formatar_mensagem("Python", "é", "sensacional!"))
print(formatar_mensagem("Item1", "Item2", "Item3", separador=" - "))
```

### Exercício 43: Ficha Técnica de Produto Dinâmica
```python
def gerar_ficha_produto(nome, preco, **especificacoes):
    print(f"\n--- Ficha Técnica: {nome} ---")
    print(f"Preço: R$ {preco:.2f}")
    print("Especificações:")
    for chave, valor in especificacoes.items():
        print(f"- {chave.capitalize()}: {valor}")
    print("-" * 30)

gerar_ficha_produto("Smartphone Ultra", 1999.90, memoria="128GB", ram="8GB", camera="64MP")
```

### Exercício 44: Calculadora de Média com Pesos Arbitrários
```python
def calcular_media_ponderada(*notas, **pesos):
    soma_ponderada = 0
    soma_pesos = 0
    for i, nota in enumerate(notas):
        chave_peso = f"p{i+1}"
        peso = pesos.get(chave_peso, 1) # Se o peso não for informado, assume 1
        soma_ponderada += nota * peso
        soma_pesos += peso
    
    return soma_ponderada / soma_pesos if soma_pesos != 0 else 0

# P1=2, P2=3, P3=5
media = calcular_media_ponderada(7.0, 8.0, 9.0, p1=2, p2=3, p3=5)
print(f"Média ponderada: {media:.2f}")
```

---

## Parte 6: Módulos, Importação e Organização de Código

### Exercício 45: Criando seu Próprio Módulo
Salve o código abaixo em um arquivo chamado `operacoes_strings.py` no mesmo diretório de execução do script principal:
```python
# Conteúdo de operacoes_strings.py

def capitalizar_tudo(texto):
    """Retorna o texto em maiúsculas."""
    return texto.upper()

def inverter_texto(texto):
    """Retorna o texto invertido de trás para a frente."""
    return texto[::-1]

def remover_espacos(texto):
    """Remove todos os espaços do texto."""
    return texto.replace(" ", "")
```

### Exercício 46: Importação Completa
```python
# Importa o módulo completo
import operacoes_strings

texto = "Estudos de Python"
# As funções precisam ser prefixadas com o nome do módulo
print(operacoes_strings.capitalizar_tudo(texto))
print(operacoes_strings.inverter_texto(texto))
print(operacoes_strings.remover_espacos(texto))
```

### Exercício 47: Importando Funções Específicas
```python
# Importa funções específicas do módulo
from operacoes_strings import capitalizar_tudo, inverter_texto

texto = "Estudos de Python"
# Chame as funções diretamente pelo nome
print(capitalizar_tudo(texto))
print(inverter_texto(texto))
```

### Exercício 48: Utilizando Alias para Funções
```python
# Importa com um apelido local
from operacoes_strings import remover_espacos as sem_espaco

texto = "Estudos de Python"
# Chame pelo alias
print(sem_espaco(texto))
```

### Exercício 49: Utilizando Alias para Módulos
```python
# Importa o módulo atribuindo um apelido
import operacoes_strings as ost

texto = "Estudos de Python"
print(ost.capitalizar_tudo(texto))
```

### Exercício 50: Importação Total com Asterisco
```python
# Importa todos os nomes expostos pelo módulo
from operacoes_strings import *

texto = "Estudos de Python"
print(capitalizar_tudo(texto))

# --- IMPACTO / DISCUSSÃO ---
# Embora pareça conveniente por não exigir prefixos, 'import *' deve ser evitado:
# 1. Colisão de Nomes (Name Clashing): Se tivermos outra função chamada 'capitalizar_tudo'
#    no nosso script principal ou importada de outro módulo, ela sobrescreverá silenciosamente
#    a função original, criando bugs extremamente difíceis de depurar.
# 2. Legibilidade Prejudicada: Outros desenvolvedores lendo o código não conseguirão identificar
#    de qual arquivo veio 'capitalizar_tudo' ou 'inverter_texto', dificultando a manutenção.
```
