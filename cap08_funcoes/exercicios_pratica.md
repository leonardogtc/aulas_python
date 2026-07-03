# Exercícios de Fixação: Capítulo 8 - Funções

Este arquivo contém 50 exercícios progressivos projetados para praticar e consolidar os conceitos de funções em Python estudados no Capítulo 8. Os exercícios estão divididos por seções temáticas e classificados por nível de dificuldade: **Fácil**, **Médio** e **Difícil**.

---

## Parte 1: Conceitos Básicos, Definição e Docstrings
*Arquivos de referência: `c08_a001.py` a `c08_a003ex.py`*

### Exercício 1: Mensagem Simples (Fácil)
Escreva uma função chamada `mostrar_mensagem()` que exiba na tela uma frase curta descrevendo o que você está aprendendo neste capítulo (por exemplo: "Neste capítulo, estou aprendendo a organizar meu código em funções reutilizáveis!"). Chame a função para testar seu funcionamento.

### Exercício 2: Saudação Personalizada (Fácil)
Escreva uma função chamada `saudar_usuario(nome)` que aceite um nome de usuário como parâmetro e exiba uma saudação personalizada (ex: "Olá, Leonardo! Seja bem-vindo ao estudo de funções!"). Chame a função passando diferentes nomes.

### Exercício 3: Documentando uma Função (Fácil)
Escreva uma função `somar_dois_numeros(a, b)` que receba dois números e exiba a soma deles. Adicione uma docstring explicativa explicando o propósito da função. Em seguida, chame a função e acesse o atributo `__doc__` da função para imprimir a documentação na tela.

### Exercício 4: Área do Quadrado (Fácil)
Escreva uma função chamada `calcular_area_quadrado(lado)` que calcule e exiba a área de um quadrado com base no lado fornecido.
*Exemplo de saída para lado = 4:* `A área do quadrado é 16.`

### Exercício 5: Conversor de Temperatura (Fácil)
Escreva uma função `celsius_para_fahrenheit(celsius)` que converta uma temperatura em graus Celsius para Fahrenheit usando a fórmula $F = C \times 1.8 + 32$. A função deve exibir a mensagem formatada: `"X°C equivale a Y°F."`

### Exercício 6: Contador de Caracteres (Médio)
Escreva uma função chamada `contar_caracteres(texto)` que conte e exiba quantos caracteres existem em um texto recebido por parâmetro. O texto exibido deve detalhar se a contagem inclui espaços em branco.
*Exemplo:* `O texto fornecido possui 25 caracteres.`

### Exercício 7: Verificação de Paridade (Médio)
Desenvolva uma função `verificar_paridade(numero)` que receba um número inteiro e exiba se ele é `"Par"` ou `"Ímpar"`. Teste a função com números positivos, negativos e com o zero.

### Exercício 8: Ajuda Interativa com Docstrings (Fácil)
Crie uma função `multiplicar_valores(x, y)` com uma docstring detalhada que descreve a utilidade da função, seus parâmetros e o tipo esperado. No final do seu script, chame a função nativa `help(multiplicar_valores)` para verificar a formatação de ajuda gerada automaticamente pelo Python.

---

## Parte 2: Parâmetros e Argumentos (Posicionais, Nomeados e Default)
*Arquivos de referência: `c08_a004.py` a `c08_a007ex.py`*

### Exercício 9: Pet Shop (Fácil)
Crie uma função chamada `descrever_pet(tipo, nome)` que exiba frases como:
1. `Eu tenho um <tipo>.`
2. `Meu <tipo> se chama <nome>.`
Chame a função passando argumentos **posicionais** (respeitando a ordem dos parâmetros).

### Exercício 10: Argumentos Nomeados (Fácil)
Utilizando a mesma função `descrever_pet(tipo, nome)` do Exercício 9, chame-a duas vezes utilizando **argumentos nomeados (keyword arguments)**. Altere a ordem dos argumentos passados na chamada e observe se o resultado se mantém correto.

### Exercício 11: Marca Padrão (Fácil)
Escreva uma função chamada `descrever_carro(modelo, marca='Chevrolet')` onde a marca possui o valor default `"Chevrolet"`. Chame a função especificando apenas o modelo e, em seguida, chame-a novamente especificando o modelo e uma marca diferente (ex: "Ford").

### Exercício 12: Confecção de Camiseta (Médio)
Escreva uma função chamada `fazer_camiseta(tamanho, estampa)` que exiba uma frase resumindo o tamanho da camiseta e a estampa escolhida.
1. Chame a função usando argumentos posicionais.
2. Chame a função usando argumentos nomeados.

### Exercício 13: Camisetas Grandes por Padrão (Médio)
Modifique a função `fazer_camiseta()` para que as camisetas sejam tamanho `"G"` por default, com a estampa `"Eu amo Python"`. Escreva chamadas para criar:
1. Uma camiseta G com a mensagem padrão.
2. Uma camiseta M com a mensagem padrão.
3. Uma camiseta PP com uma estampa personalizada de sua escolha.

### Exercício 14: Descrição de Cidades (Médio)
Escreva uma função chamada `descrever_cidade(cidade, pais='Brasil')` que exiba uma frase simples como: `"<cidade> fica no(a) <pais>."`
Chame a função para três cidades diferentes, garantindo que pelo menos uma delas não fique no país padrão (Brasil).

### Exercício 15: Cálculo de Preço com Desconto Opcional (Médio)
Crie uma função `calcular_preco(nome_produto, preco_original, desconto=0.0)` que calcule e mostre o preço final de um produto. Se o desconto não for passado, ele deve ser considerado zero. A saída deve ser semelhante a: `"Produto: <nome>, Preço Final: R$<valor>."`

### Exercício 16: O Impacto da Ordem dos Posicionais (Médio)
Defina uma função `apresentar_idade(nome, idade)`. Mostre em um exemplo prático de código o que acontece se você chamar a função invertendo os valores sem nomeá-los (por exemplo, passando a idade no lugar do nome e vice-versa). O Python gera algum erro ou a saída fica apenas semanticamente incorreta?

### Exercício 17: Ficha de Endereço Completa (Difícil)
Escreva uma função `exibir_endereco(rua, cidade, estado, cep, numero='S/N')` que formate e mostre um endereço. Note que o número deve vir por padrão como `"S/N"`. Faça chamadas passando argumentos mistos (posicionais e nomeados) para testar a flexibilidade dos parâmetros.

---

## Parte 3: Retorno de Valores
*Arquivos de referência: `c08_a008.py` a `c08_a012ex.py`*

### Exercício 18: Formatando Nome Completo (Fácil)
Escreva uma função chamada `obter_nome_formatado(nome, sobrenome)` que receba esses dois termos e **retorne** uma string formatada de forma elegante com as primeiras letras maiúsculas (`title()`). Imprima o resultado retornado.

### Exercício 19: Nome do Meio Opcional (Médio)
Modifique a função `obter_nome_formatado` para que ela possa aceitar um parâmetro opcional `nome_do_meio`. Esse parâmetro deve vir por padrão como uma string vazia (`''`). Teste a função chamando-a com dois e com três nomes.

### Exercício 20: Dicionário de Cadastro de Usuário (Médio)
Escreva uma função chamada `construir_usuario(nome, email, telefone)` que receba as informações e retorne um dicionário representando esse usuário. Exiba no console o dicionário retornado.

### Exercício 21: Cadastro com Campo Opcional (Médio)
Modifique a função `construir_usuario` para aceitar um parâmetro opcional `idade` (valor padrão `None` ou vazio). Se a idade for fornecida, ela deve ser incluída no dicionário retornado; caso contrário, a chave `idade` não deve fazer parte do dicionário.

### Exercício 22: Operações Matemáticas Básicas (Médio)
Escreva uma função chamada `calcular_operacoes(a, b)` que retorne a soma, a subtração, a multiplicação e a divisão de `a` por `b` em uma única instrução de retorno (retornando uma tupla ou dicionário). Demonstre como desempacotar os valores retornados no código principal.

### Exercício 23: Retornando o Maior de Três Números (Fácil)
Crie uma função `encontrar_maior(n1, n2, n3)` que compare três números fornecidos como argumentos e retorne o maior valor entre eles.

### Exercício 24: Cidade e País Formatados (Fácil)
Escreva uma função chamada `cidade_pais(cidade, pais)` que retorne uma string formatada como `"Valparaíso, Chile"`. Chame a função com pelo menos três pares diferentes de cidade-país e exiba o resultado na tela.

### Exercício 25: Cadastro de Álbuns Musicais (Médio)
Escreva uma função chamada `make_album(artista, titulo, faixas=None)` que construa um dicionário descrevendo um álbum musical. A função deve aceitar o nome do artista, o título do álbum e um número opcional de faixas. Chame a função para criar três dicionários representando álbuns diferentes.

### Exercício 26: Cadastro com Loop While (Difícil)
Comece com a função `make_album` criada no Exercício 25. Escreva um laço `while` que permita aos usuários inserir o artista e o título de um álbum de forma interativa. Certifique-se de incluir um valor de saída (como digitar `'q'`) para interromper o laço. A cada ciclo do laço, chame a função e imprima o dicionário gerado.

---

## Parte 4: Passando e Modificando Listas em Funções
*Arquivos de referência: `c08_a013.py` a `c08_a017ex.py`*

### Exercício 27: Mensagens em Massa (Fácil)
Crie uma lista contendo várias mensagens curtas. Escreva uma função chamada `exibir_mensagens(lista_mensagens)` que percorra a lista usando um laço e exiba cada mensagem individualmente.

### Exercício 28: Enviando Mensagens (Médio)
Comece com uma cópia do seu código do Exercício 27. Escreva uma função chamada `enviar_mensagens(lista_pendentes, lista_enviadas)` que simule o envio de cada mensagem da primeira lista:
1. Exiba a mensagem que está sendo enviada.
2. Mova a mensagem para a lista `lista_enviadas`.
No final, imprima ambas as listas para confirmar que as mensagens foram movidas corretamente.

### Exercício 29: Preservando a Lista Original (Médio)
Utilize as listas e as funções do Exercício 28. Chame a função `enviar_mensagens` passando uma **cópia** da lista de mensagens pendentes, de modo que a lista original permaneça inalterada após a execução da função. Imprima as duas listas originais para provar que a lista de pendentes inicial não foi esvaziada.

### Exercício 30: Dobrar Valores de uma Lista (Médio)
Escreva uma função chamada `dobrar_valores(numeros)` que receba uma lista de inteiros e altere os seus elementos diretamente na lista original multiplicando-os por 2 (modificação *in-place*). Demonstre que a lista original foi alterada fora da função.

### Exercício 31: Filtrar Números Pares (Médio)
Escreva uma função chamada `filtrar_pares(numeros)` que receba uma lista de inteiros e retorne uma **nova lista** contendo apenas os números pares. Mostre que a lista original passada como argumento continuou idêntica.

### Exercício 32: Atualização de Status (Médio)
Escreva uma função `atualizar_status_pedidos(pedidos)` que receba uma lista de dicionários (cada dicionário representa um pedido com as chaves `'id'` e `'status'`). A função deve alterar o status de todos os pedidos na lista para `"Concluído"`.

### Exercício 33: Mágicos e Grandes Mágicos (Médio)
Crie uma lista de nomes de mágicos.
1. Escreva uma função chamada `show_magicians(magicos)` que imprima o nome de cada mágico.
2. Escreva uma função `make_great(magicos)` que modifique a lista acrescentando a expressão `"o Grande"` ao final do nome de cada mágico. Chame as funções para ver se a lista foi alterada.

### Exercício 34: Evitando Grandes Mágicos Inalterados (Difícil)
Chame a função `make_great` com uma cópia da lista de mágicos do Exercício 33. Guarde a lista modificada retornada em uma nova variável. Exiba a lista original e a nova lista modificada para comprovar a independência entre as duas.

### Exercício 35: Analisador de Listas (Difícil)
Crie uma função `analisar_notas(notas)` que receba uma lista de notas e retorne um dicionário contendo: a maior nota, a menor nota, a média das notas e se o aluno foi aprovado (média >= 7.0).

---

## Parte 5: Argumentos Arbitrários (`*args` e `**kwargs`)
*Arquivos de referência: `c08_a018.py` a `c08_a022ex.py`*

### Exercício 36: Pedido de Sanduíche (`*args`) (Fácil)
Escreva uma função que aceita uma série de itens que uma pessoa deseja em um sanduíche. A função deve ter apenas um parâmetro que agrupe todos os itens fornecidos na chamada da função (`*itens`) e deve imprimir um resumo do sanduíche pedido.

### Exercício 37: Várias Chamadas de Sanduíches (Fácil)
Chame a função criada no Exercício 36 três vezes, usando um número de ingredientes diferente em cada chamada (ex: 1 ingrediente, 3 ingredientes, 5 ingredientes).

### Exercício 38: Misturando Tamanho e Ingredientes (Médio)
Modifique a função do sanduíche para aceitar também um tamanho fixo (ex: "Pequeno", "Médio", "Grande") como argumento posicional antes do parâmetro que agrupa os ingredientes. Faça chamadas válidas para testar a combinação.

### Exercício 39: Somador Infinito (Médio)
Crie uma função chamada `somar_todos(*numeros)` que aceite uma quantidade arbitrária de números e retorne a soma de todos eles. Teste com 0, 1, 5 e 10 números.

### Exercício 40: Perfil de Usuário (`**kwargs`) (Médio)
Escreva uma função `construir_perfil(nome, sobrenome, **informacoes)` que receba o nome, sobrenome e outros dados arbitrários (chave-valor). A função deve retornar um dicionário completo com todas as informações unificadas.

### Exercício 41: Cadastro de Carros (`**kwargs`) (Médio)
Escreva uma função que armazene informações sobre um carro em um dicionário. A função deve sempre receber o fabricante e o modelo, mas deve aceitar também um número arbitrário de argumentos nomeados (ex: cor, ano, opcionais). Chame a função com as informações necessárias e dois outros pares chave-valor.

### Exercício 42: Concatenação Inteligente de Strings (Médio)
Crie uma função `formatar_mensagem(*palavras, separador=' ')` que receba uma quantidade indefinida de palavras e as junte em uma única string usando o `separador` especificado como argumento nomeado padrão.

### Exercício 43: Ficha Técnica de Produto Dinâmica (Difícil)
Escreva uma função `gerar_ficha_produto(nome, preco, **especificacoes)` que receba obrigatoriamente o nome e preço do produto, e monte uma ficha técnica formatada a partir das especificações passadas dinamicamente. Imprima o resultado na tela de forma legível.

### Exercício 44: Calculadora de Média com Pesos Arbitrários (Difícil)
Crie uma função `calcular_media_ponderada(*notas, **pesos)`. A função recebe uma quantidade indefinida de notas e um dicionário de pesos correspondente a cada nota. Calcule a média ponderada e retorne-a.

---

## Parte 6: Módulos, Importação e Organização de Código
*Arquivo de referência: `c08_a023.py`*

### Exercício 45: Criando seu Próprio Módulo (Fácil)
Crie um arquivo chamado `operacoes_strings.py` contendo pelo menos três funções de manipulação de strings de sua escolha (ex: `capitalizar_tudo(texto)`, `inverter_texto(texto)`, `remover_espacos(texto)`).

### Exercício 46: Importação Completa (Fácil)
Crie um segundo arquivo Python na mesma pasta chamado `principal.py`. Importe o módulo `operacoes_strings` de forma completa usando `import operacoes_strings` e chame todas as funções criadas no Exercício 45.

### Exercício 47: Importando Funções Específicas (Fácil)
No arquivo `principal.py`, modifique a importação para obter apenas uma ou duas funções específicas do módulo usando a sintaxe `from modulo import funcao`. Execute chamadas diretas às funções sem prefixar o nome do módulo.

### Exercício 48: Utilizando Alias para Funções (Fácil)
Modifique o arquivo `principal.py` para importar uma das funções do módulo `operacoes_strings` atribuindo-lhe um apelido (alias) curto ou em português usando a palavra reservada `as`. Demonstre a chamada da função pelo seu alias.

### Exercício 49: Utilizando Alias para Módulos (Fácil)
No arquivo `principal.py`, importe o módulo `operacoes_strings` utilizando um alias para o módulo inteiro (ex: `import operacoes_strings as ost`). Chame as funções do módulo por meio desse alias.

### Exercício 50: Importação Total com Asterisco (Médio)
No arquivo `principal.py`, faça a importação de todas as funções do módulo `operacoes_strings` utilizando a sintaxe `from modulo import *`. Comente no próprio código qual é o impacto desse tipo de importação em projetos grandes e quais problemas podem surgir devido à colisão de nomes.
