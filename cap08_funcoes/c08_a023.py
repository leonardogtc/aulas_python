# Armazenando suas funções em módulos
# -------------------------------------
# Uma vantagem das funções é a maneira como elas separam blocos de
# código de seu programa principal. Ao usar nomes descritivos para suas
# funções, será bem mais fácil entender o seu programa principal. Você pode
# dar um passo além armazenando suas funções em um arquivo separado
# chamado módulo e, então, importar esse módulo em seu programa
# principal. Uma instrução import diz a Python para deixar o código de um
# módulo disponível no arquivo de programa em execução no momento.
# Armazenar suas funções em um arquivo separado permite ocultar os
# detalhes do código de seu programa e se concentrar na lógica de nível mais
# alto. Também permite reutilizar funções em muitos programas diferentes.
# Quando armazenamos funções em arquivos separados, podemos
# compartilhar esses arquivos com outros programadores sem a necessidade
# de compartilhar o programa todo. Saber como importar funções também
# possibilita usar bibliotecas de funções que outros programadores
# escreveram.
# Há várias maneiras de importar um módulo e vou mostrar cada uma
# delas rapidamente.

from c08_a020 import pizza  # Importando uma função específica de um módulo
from c08_a019 import fazer_pizza  # Importando apenas a função necessária

# Criar um alias para importar o módulo com um nome mais curto
import c08_a021 as perfil


pizza('familía', 'cogumelos', 'pimentões verdes', 'queijo extra')

user_profile = perfil.criar_perfil(
    'albert', 'einstein', location='princeton', field='physics')

print(user_profile)

fazer_pizza('cogumelos', 'pimentões verdes', 'queijo extra')
