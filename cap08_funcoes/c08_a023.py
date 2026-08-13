# CONCEITO: Módulos e Importação de Funções (import)
# ----------------------------------------------------
# Um módulo é simplesmente um arquivo com extensão .py contendo funções e definições.
# Ao importar módulos em seu programa principal, você pode reutilizar códigos de outros arquivos
# mantendo seu script principal limpo e legível.

# Forma 1: Importando uma função específica de outro arquivo/módulo usando `from modulo import funcao`
from c08_a020 import pizza  # Importa apenas a função 'pizza' definida no arquivo c08_a020.py

# Forma 2: Importando outra função de outro módulo
from c08_a019 import fazer_pizza  # Importa a função 'fazer_pizza' de c08_a019.py

# Forma 3: Importando um módulo inteiro e atribuindo um ALIAS (apelido) com `as`
import c08_a021 as perfil  # Permite acessar funções do c08_a021 usando a sintaxe 'perfil.nome_funcao()'


# --- EXECUTANDO AS FUNÇÕES IMPORTADAS ---

# Usando a função 'pizza' importada diretamente de c08_a020
pizza('família', 'cogumelos', 'pimentões verdes', 'queijo extra')

# Usando a função 'criar_perfil' através do alias do módulo 'perfil' (c08_a021)
user_profile = perfil.criar_perfil(
    'albert', 'einstein', location='princeton', field='physics')
print(user_profile)

# Usando a função 'fazer_pizza' importada de c08_a019
fazer_pizza('cogumelos', 'pimentões verdes', 'queijo extra')
