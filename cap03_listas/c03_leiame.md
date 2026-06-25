# Listas
## Notas

### O que é uma lista?
- As listas permitem armazenar conjuntos de informações em um só lugar, independentemente de termos alguns itens ou milhões deles.
- Uma lista é uma coleção de itens em uma ordem em particular.
- Você pode colocar qualquer informação que quiser em uma lista, e os itens de sua lista não precisam estar relacionados de nenhum modo em particular.
- Como uma lista geralmente contém mais de um elemento, é uma boa ideia deixar seu nome no plural
- Em Python, colchetes ([]) indicam uma lista, e elementos individuais da lista são separados por vírgulas.

## Acessando elementos de uma lista
- Listas são coleções ordenadas, portanto você pode acessar qualquer elemento de uma lista informando a posição - ou índice - do item desejado.
- Para acessar um elemento de uma lista escreva o nome da lista seguido do índice entre colchetes. 
- O valor do índice é numérico começando por zero que indica o primeiro elemento da lista.

## A posição dos índices começa em 0, e não em 1
- Python considera que o primeiro item de uma lista está na posição 0, e não na posição 1. Isso é válido para a maioria das linguagens de programação, e o motivo tem a ver com o modo como as operações em lista são implementadas em um nível mais baixo.

### Acessando o último elemento de uma lista
- Python tem uma sintaxe especial para acessar o último elemento de uma lista. Ao solicitar o item no índice -1, Python sempre devolve o último item da lista:

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])

- O índice -2 devolve o segundo item a partir do final da lista, o índice -3 devolve o terceiro item a partir do final, e assim sucessivamente.

### Usando valores individuais

- Você pode usar valores individuais de uma lista, exatamente como faria com qualquer outra variável.

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

(Parada para exercícios)

## Alterando, acrescentando e removendo elementos
- A maioria das listas que você criar serão dinâmicas, o que significa que você criará uma lista e então adicionará e removerá elementos dela à medida que seu programa executar.
- Exemplo: você poderia criar um jogo em que um jogador atire em alienígenas que caem do céu. Poderia armazenar o conjunto inicial de alienígenas em uma lista e então remover um item da lista sempre que um alienígena for atingido. Sempre que um novo alienígena aparecer na tela, adicione-o à lista. Sua lista de alienígenas diminuirá e aumentará de tamanho no decorrer do jogo.

### Modificando elementos de uma lista
A sintaxe para modificar um elemento é semelhante à sintaxe para acessar um elemento de uma lista. Para alterar um elemento, use o nome da lista seguido do índice do elemento que você quer modificar e, então, forneça o novo valor que você quer que esse item tenha.

### Acrescentando elementos em uma lista
- Você pode acrescentar um novo elemento em uma lista por diversos motivos. Por exemplo, talvez você queira que novos alienígenas apareçam no jogo, pode querer acrescentar novos dados em uma visualização ou adicionar novos usuários registrados em um site que você criou.

#### Concatenando elementos no final de uma lista
- A maneira mais simples de acrescentar um novo elemento em uma lista é concatenar o item na lista.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

O método append() em u acrescenta 'ducati' no final da lista sem afetar qualquer outro elemento:

['honda', 'yamaha', 'suzuki']
['honda', 'yamaha', 'suzuki', 'ducati']

- O método append() facilita criar listas dinamicamente.
Exemplo: podemos começar com uma lista vazia e então acrescentar itens à lista usando uma série de instruções append().

motocicletas = []
print(motocicletas)

''' Adicionando elementos '''
motocicletas.append('honda')
motocicletas.append('yamaha')
motocicletas.append('suzuki')

print(motocicletas)

#### Inserindo elementos em uma lista
- Você pode adicionar um novo elemento em qualquer posição de sua lista usando o método insert(). Faça isso especificando o índice do novo elemento e o valor do novo item.

motocicletas.insert(0, 'ducati')
print(motocicletas)
['ducati', 'honda', 'yamaha', 'suzuki']

### Removendo elementos de uma lista
- Se a posição do item que você quer remover de uma lista for conhecida, a instrução del poderá ser usada.

del.motocicletas[1]

- Você pode remover um item de qualquer posição em uma lista usando a
instrução del, se souber qual é o seu índice.

### Removendo um item com o método pop()
Nota: Às vezes, você vai querer usar o valor de um item depois de removê-lo de uma lista. Por exemplo, talvez você queira obter as posições x e y de um alienígena que acabou de ser atingido para que possa desenhar uma explosão nessa posição. Em uma aplicação web, você poderia remover um usuário de uma lista de membros ativos e então adicioná-lo a uma lista de membros inativos.
O método pop() remove o último item de uma lista, mas permite que você trabalhe com esse item depois da remoção.

# Removendo itens de qualquer posição


-----------------







































