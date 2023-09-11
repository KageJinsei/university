# criando um jogo de jokenpô

from random import randint

def validaInt(pergunta, min, max):

    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def vencedor(jogador1, jogador2):
    global empate, vencedor1, vencedor2
    if (jogador1 == 1): # Pedra
        if (jogador2 == 1): # Pedra
            empate += 1
        elif (jogador2 == 2): # Papel
            jogador2 += 1
        elif (jogador2 == 3): # Tesoura
            jogador1 += 1
    elif (jogador1 == 2): # Papel
        if (jogador2 == 1): # Pedra
            jogador1 += 1
        elif (jogador2 == 2): # Papel
            empate += 1
        elif (jogador2 == 3): # Tesoura
            jogador2 += 1
    elif (jogador1 == 3): # Tesoura
        if (jogador2 == 1): # Pedra
            jogador2 += 1
        elif (jogador2 == 2): # Papel
            jogador1 += 1
        elif (jogador2 == 3): # Tesoura
            empate += 1
    resultados = [vitoriasJ1, vitoriasJ2, empate]
    return resultados

# Main

print('JOKENPÔ')
print('1 - Pedra\n' +
      '2 - Papel\n' +
      '3 - Tesoura')

resultados = []
jogadas = []
vitoriasJ1 = 0
vitoriasJ2 = 0
empate = 0

while True:
    j1 = validaInt('Escolha a sua jogada: ', 0, 3)
    if (not j1):
        break
    j2 = randint(1, 3)
    jogadas.append([j1, j2])
    resultados = vencedor(j1, j2)

    for jogada in jogadas:
        for dado in jogada:
            print(dado, end=' ')
        print()

print(f'Número de vitórias do jogador 1: {resultados[0]}')
print(f'Número de vitórias do jogador 2: {resultados[1]}')
print(f'Número de empates: {resultados[2]}')