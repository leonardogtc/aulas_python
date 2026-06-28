# ==============================================================================
# EXERCÍCIOS GERAIS - CAPÍTULO 6: DICIONÁRIOS
# ==============================================================================
# Resolva os exercícios abaixo para praticar o uso de dicionários em Python.
# Cada exercício possui seu enunciado. Escreva a solução logo abaixo dele.
# ==============================================================================

# ------------------------------------------------------------------------------
# PARTE 1: OPERAÇÕES BÁSICAS COM DICIONÁRIOS
# (Criação, Acesso, Modificação, Adição e Remoção)
# ------------------------------------------------------------------------------

# 1. Cadastro Simples: Crie um dicionário chamado 'produto' para armazenar
# as informações de um item (nome, preco e quantidade). Em seguida, exiba
# cada informação separadamente acessando as respectivas chaves.
# Escreva seu código aqui:


# 2. Atualização de Dados: Com base no dicionário 'produto' criado no exercício
# anterior, atualize o preço para um novo valor e aumente a quantidade em 5 unidades.
# Exiba o dicionário atualizado.
# Escreva seu código aqui:


# 3. Adição de Nova Chave: Adicione uma nova chave chamada 'categoria' (por exemplo,
# 'Eletrônicos', 'Alimentos') ao dicionário 'produto'. Exiba o dicionário final.
# Escreva seu código aqui:


# 4. Remoção de Chave: Remova a chave 'quantidade' do dicionário 'produto' usando
# o comando 'del' ou o método '.pop()'. Exiba o dicionário após a remoção.
# Escreva seu código aqui:


# 5. Dicionário de Contatos: Crie um dicionário chamado 'contatos' contendo o nome
# de 5 amigos como chaves e seus números de telefone (strings) como valores.
# Escreva seu código aqui:


# ------------------------------------------------------------------------------
# PARTE 2: PERCORRENDO DICIONÁRIOS COM LAÇOS (LOOPS)
# (Métodos .items(), .keys(), .values() e ordenação)
# ------------------------------------------------------------------------------

# 6. Percorrendo Chaves e Valores: Use um laço 'for' e o método '.items()' para
# percorrer o dicionário 'contatos' criado no exercício 5. Exiba uma frase formatada
# para cada contato, por exemplo: "O telefone de [Nome] é [Telefone]."
# Escreva seu código aqui:


# 7. Apenas as Chaves: Use um laço 'for' e o método '.keys()' para exibir
# apenas os nomes de todos os amigos cadastrados no dicionário 'contatos'.
# Escreva seu código aqui:


# 8. Apenas os Valores: Use um laço 'for' e o método '.values()' para exibir
# todos os números de telefone salvos no dicionário 'contatos'.
# Escreva seu código aqui:


# 9. Chaves Ordenadas: Crie um dicionário chamado 'linguagens_favoritas' com o nome
# de 5 pessoas e suas respectivas linguagens de programação preferidas. Use um laço
# 'for' junto com a função 'sorted()' para exibir os nomes dos participantes em ordem alfabética.
# Escreva seu código aqui:


# 10. Valores Únicos: Utilizando o dicionário 'linguagens_favoritas' do exercício anterior
# (certifique-se de que há linguagens repetidas entre as pessoas), use a função 'set()'
# em um laço 'for' para exibir apenas as linguagens citadas, sem repetições.
# Escreva seu código aqui:


# ------------------------------------------------------------------------------
# PARTE 3: MÉTODOS E OPERAÇÕES ÚTEIS
# (Uso de .get(), operador 'in', .update(), .clear() e len())
# ------------------------------------------------------------------------------

# 11. Tratamento com get(): Crie um dicionário representando um 'usuario' (com nome e email).
# Tente exibir o valor da chave 'ultimo_acesso'. Para evitar um erro de chave (KeyError),
# utilize o método '.get()' com um valor padrão amigável como "Nunca acessou".
# Escreva seu código aqui:


# 12. Verificação de Chave com 'in': Verifique se a chave 'email' existe no seu
# dicionário de 'usuario' usando o operador 'in'. Se não existir, adicione-a. Se existir,
# mostre uma mensagem confirmando sua existência.
# Escreva seu código aqui:


# 13. Fusão de Dicionários: Crie dois dicionários: 'estoque_a' e 'estoque_b',
# cada um contendo alguns produtos e suas quantidades. Use o método '.update()' para
# mesclar o conteúdo de 'estoque_b' em 'estoque_a' e exiba 'estoque_a'.
# Escreva seu código aqui:


# 14. Limpeza de Dicionário: Crie um dicionário 'carrinho' representando produtos adicionados
# temporariamente por um cliente. Simule a ação de esvaziar o carrinho limpando todos
# os dados do dicionário usando o método '.clear()'. Exiba o dicionário após a limpeza.
# Escreva seu código aqui:


# 15. Contando Elementos: Crie um dicionário de 'notas_aluno' mapeando disciplinas a suas notas.
# Use a função 'len()' para descobrir e imprimir a quantidade total de matérias que o aluno está cursando.
# Escreva seu código aqui:


# ------------------------------------------------------------------------------
# PARTE 4: ANINHAMENTO (NESTING) - LISTA DE DICIONÁRIOS
# ------------------------------------------------------------------------------

# 16. Lista de Dicionários: Crie três dicionários diferentes, cada um representando um
# personagem de um jogo (com chaves 'nome', 'classe' e 'nivel'). Armazene esses dicionários
# em uma lista chamada 'personagens'. Percorra a lista com um laço 'for' e exiba os detalhes de cada um.
# Escreva seu código aqui:


# 17. Geração Dinâmica de Dicionários: Crie uma lista vazia chamada 'inimigos'. Use um laço
# 'for' para criar e adicionar 10 dicionários de inimigos idênticos à lista. Cada inimigo
# deve ter as chaves 'vida': 100 e 'forca': 15.
# Escreva seu código aqui:


# 18. Modificando Dicionários em uma Lista: Utilizando a lista 'inimigos' do exercício anterior,
# use um laço 'for' com fatiamento para alterar o valor da chave 'forca' para 30 e 'vida' para 150
# apenas para os 3 primeiros inimigos da lista. Exiba a lista final de inimigos.
# Escreva seu código aqui:


# 19. Filtrando Lista de Dicionários: Crie uma lista com 4 dicionários de carros. Cada carro deve
# ter as chaves 'marca', 'modelo' e 'ano'. Percorra a lista e exiba apenas os modelos dos carros
# fabricados a partir do ano de 2021.
# Escreva seu código aqui:


# 20. Busca em Lista de Dicionários: Crie uma lista contendo dicionários de 'livros' (chaves:
# 'titulo', 'autor', 'paginas'). Peça para o usuário digitar o nome de um autor e procure
# na lista se há livros desse autor, exibindo seus títulos.
# Escreva seu código aqui:


# ------------------------------------------------------------------------------
# PARTE 5: ANINHAMENTO (NESTING) - LISTAS DENTRO DE DICIONÁRIOS
# ------------------------------------------------------------------------------

# 21. Lista dentro de Dicionário (Pedido de Pizza): Crie um dicionário 'pizza' com as chaves
# 'borda' (ex: 'catupiry') e 'ingredientes' (uma lista de strings contendo os ingredientes).
# Exiba uma frase resumindo o pedido de forma organizada, listando os ingredientes um a um.
# Escreva seu código aqui:


# 22. Desenvolvedores e Tecnologias: Crie um dicionário chamado 'dev_techs' onde as chaves são nomes
# de desenvolvedores e os valores são listas contendo as tecnologias que eles dominam.
# Percorra o dicionário exibindo o nome de cada desenvolvedor e, em seguida, faça um laço
# interno para listar cada tecnologia com uma indentação elegante.
# Escreva seu código aqui:


# 23. Enquete de Hobbies: Crie um dicionário 'hobbies' onde as chaves são nomes de amigos e os
# valores são listas de seus hobbies. Use um laço 'for' para exibir o nome do amigo e diga
# quantos hobbies ele possui (usando 'len()' na lista de hobbies).
# Escreva seu código aqui:


# 24. Notas e Média: Crie um dicionário 'boletim' onde as chaves são os nomes dos alunos e
# os valores são listas contendo 4 notas de provas. Percorra o dicionário, calcule a média
# das notas de cada aluno e exiba uma frase como: "A média de [Aluno] é [Media]".
# Escreva seu código aqui:


# 25. Roteiro de Viagens: Crie um dicionário chamado 'plano_viagem' com chaves 'destino' e 'pontos_turisticos'
# (sendo este último uma lista de locais que deseja visitar). Exiba o destino principal e depois exiba os
# pontos turísticos em linhas separadas pré-formatadas com marcadores (ex: " * Estátua da Liberdade").
# Escreva seu código aqui:


# ------------------------------------------------------------------------------
# PARTE 6: ANINHAMENTO (NESTING) - DICIONÁRIOS DENTRO DE DICIONÁRIOS
# ------------------------------------------------------------------------------

# 26. Cadastro de Usuários Complexo: Crie um dicionário chamado 'usuarios' onde cada chave é um
# nome de usuário exclusivo (ex: 'jdoe123', 'mario_bros') e o valor é outro dicionário contendo
# 'nome', 'sobrenome' e 'email'. Percorra o dicionário 'usuarios' e exiba as informações formatadas de cada um.
# Escreva seu código aqui:


# 27. Catálogo de Filmes: Crie um dicionário 'catalogo_filmes' onde as chaves são títulos de filmes e
# os valores são dicionários com chaves: 'diretor', 'ano' e 'genero'. Use um laço para apresentar
# todos os filmes catalogados e suas informações de maneira estruturada.
# Escreva seu código aqui:


# 28. Dicionário de Países: Crie um dicionário chamado 'paises' onde as chaves são nomes de países.
# O valor associado a cada país deve ser um dicionário com chaves 'capital', 'populacao_milhoes' e
# 'idioma_oficial'. Percorra este dicionário e exiba as curiosidades de cada país.
# Escreva seu código aqui:


# 29. Gerenciamento de Estoque de Lojas: Crie um dicionário 'estoque_filiais' contendo nomes de filiais
# (ex: 'Matriz', 'Filial Centro') como chaves. Os valores correspondentes devem ser dicionários que
# mapeiam produtos (ex: 'camiseta', 'calca') a suas respectivas quantidades em estoque.
# Percorra as filiais mostrando a quantidade de cada produto em cada uma delas.
# Escreva seu código aqui:


# 30. Agenda de Contatos Detalhada: Crie um dicionário chamado 'agenda_vip' onde cada chave é o nome
# de uma pessoa e cada valor é um dicionário contendo 'telefones' (uma lista de telefones) e 'endereco'
# (um dicionário contendo 'rua', 'cidade' e 'estado'). Escreva um script que percorra a agenda e exiba
# todas as informações de forma extremamente organizada e legível.
# Escreva seu código aqui:
