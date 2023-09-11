game = {}
games = []

for i in range(3):
    game ['nome'] = input('Qual o nome do jogo?: ')
    game ['plataforma'] = input('Para qual plataforma ele foi lançado?: ')
    game ['ano'] = input('Qual o ano de lançamento?: ')
    games.append(game.copy())
print('-' * 20)
for e in games:
    for i, j in e.items():
        print(f'O campo {i} tem o valor {j}.')   