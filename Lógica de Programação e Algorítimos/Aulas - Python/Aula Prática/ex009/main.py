totalPessoas = 0
dinheiro = 0

while True:
    idade = input('Qual é a sua idade?: ')
    if (idade == 'sair'):
        break
    idade = int(idade)
    totalPessoas += 1

    if (idade < 3):
        ingresso = 0
    else:
        if (idade > 12):
            ingresso = 30
        else:
            ingresso = 15

    dinheiro += ingresso

media = dinheiro / totalPessoas
print(f'Total de pessoas: {totalPessoas}')
print(f'Total arrecadado: {dinheiro}')
print(f'Média arrecadada: {media}')