# ----- Começando com um dicionário vazio -----

alien_0 = {}

# Acrescentando para chave:valor
alien_0['cor'] = 'verde'
alien_0['pontos'] = 5

print(alien_0)

# ----- Modificando valores em um dicionário -----
print(f"A cor do Alien é {alien_0['cor']}.")

alien_0['cor'] = 'amarelo'

print(f"A cor do Alien é {alien_0['cor']}.")

# ----- Modificando a posição do Alien -----
alien_0 = {
    'x_position': 0,
    'y_position': 25,
    'speed': 'medium'
}

# Movendo o Alien para a direita e determinar a distância em
# que deve se deslocar dependendo da velocidade atual.
if alien_0['speed'] == 'slow':
    incremento_x = 1
elif alien_0['speed'] == 'medium':
    incremento_x = 2
else:
    incremento_x = 3

# Posição final
alien_0['x_position'] = alien_0['x_position'] + incremento_x

# Mostrando resultado
print("A nova posição de x é " + str(alien_0['x_position']))
