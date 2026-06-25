'''
Um exemplo mais realista envolveria mais de três alienígenas, com um
código que gere automaticamente cada alienígena. No exemplo a seguir,
usamos range() para criar uma frota de 30 alienígenas:
'''

# Criar uma lista vazia
aliens = []

# Criar 30 alienigenas verdes
for alien_number in range(30):
    new_alien = {'cor': 'verde', 'pontos': 5, 'velocidade': 'lento'}
    aliens.append(new_alien)

# Modificar a cor dos 3 primeiros
'''
Como queremos modificar os três primeiros alienígenas, percorremos
uma fatia que inclui apenas os três primeiros alienígenas. Todos os
alienígenas são verdes agora, mas isso nem sempre ocorrerá, portanto
escrevemos uma instrução if para garantir que estamos modificando
apenas os alienígenas verdes.
'''
for alien in aliens[0:3]:
    if alien['cor'] == 'verde':
        alien['cor'] = 'amarelo'
        alien['velocidade'] = 'média'
        alien['pontos'] = 10

# Mostra os cinco primeiros
for alien in aliens[:5]:
    print(alien)
print("...")

# Mostra quantos alienigenas foram criados
print(f"Total de alienigenas criados foi de {len(aliens)} alienigenas.")
